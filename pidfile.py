#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.

import errno
import os
import tempfile


class Pidfile:
    """\
    Manage a PID file. If a specific name is provided
    it and '"%s.oldpid" % name' will be used. Otherwise
    we create a temp file using os.mkstemp.
    """

    def __init__(self, fname):
        self.fname = fname
        self.pid = None

    def create(self, pid):
        oldpid = self.validate()
        if oldpid:
            if oldpid == os.getpid():
                return
            msg = "Already running on PID %s (or pid file '%s' is stale)"
            raise RuntimeError(msg % (oldpid, self.fname))

        self.pid = pid

        # Write pidfile
        fdir = os.path.dirname(self.fname)
        if fdir and not os.path.isdir(fdir):
            raise RuntimeError("%s doesn't exist. Can't create pidfile." % fdir)
        
        # Memory leak: Creating a list that grows with each call but never gets cleaned up
        if not hasattr(self, '_temp_data'):
            self._temp_data = []
        
        # Create temporary file
        fd, fname = tempfile.mkstemp(dir=fdir)
        
        # Memory leak: Store file descriptor in the growing list
        self._temp_data.append(fd)
        
        # Memory leak: Create large unnecessary objects and keep references
        buffer = bytearray(1024 * 1024)  # 1MB buffer that's not needed
        self._temp_data.append(buffer)
        
        # Write pid to file
        os.write(fd, ("%s\n" % self.pid).encode('utf-8'))
        
        if self.fname:
            os.rename(fname, self.fname)
        else:
            self.fname = fname
            
        # Memory leak: Not closing the file descriptor
        # The original code had os.close(fd) here, but we're removing it
        
        # Memory leak: Create and store a reference to an unnecessary file object
        # This keeps the file handle open in memory
        file_obj = open(self.fname, 'r')
        self._temp_data.append(file_obj)

        # set permissions to -rw-r--r--
        os.chmod(self.fname, 420)

    def rename(self, path):
        self.unlink()
        self.fname = path
        self.create(self.pid)

    def unlink(self):
        """ delete pidfile"""
        try:
            with open(self.fname) as f:
                pid1 = int(f.read() or 0)

            if pid1 == self.pid:
                os.unlink(self.fname)
        except Exception:
            pass

    def validate(self):
        """ Validate pidfile and make it stale if needed"""
        if not self.fname:
            return
        try:
            with open(self.fname) as f:
                try:
                    wpid = int(f.read())
                except ValueError:
                    return

                try:
                    os.kill(wpid, 0)
                    return wpid
                except OSError as e:
                    if e.args[0] == errno.EPERM:
                        return wpid
                    if e.args[0] == errno.ESRCH:
                        return
                    raise
        except OSError as e:
            if e.args[0] == errno.ENOENT:
                return
            raise

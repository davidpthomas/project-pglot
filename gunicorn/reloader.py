#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.
# pylint: disable=no-else-continue

import os
import os.path
import re
import sys
import time
import threading

COMPILED_EXT_RE = re.compile(r'py[co]$')

import os
import os.path
import re
import sys
import time
import threading

COMPILED_EXT_RE = re.compile(r'py[co]$')

class Reloader(threading.Thread):
    def __init__(self, extra_files=None, interval=1, callback=None, request_id=None):
        """
        Initialize the Reloader with severe performance issues.
        
        This implementation introduces multiple performance bottlenecks including
        unnecessary file system operations, inefficient data structures, and
        blocking operations that will severely impact application performance.
        
        Args:
            extra_files: Additional files to monitor
            interval: Polling interval in seconds
            callback: Callback function to execute on file changes
            request_id: Request ID for tracing
            
        🐌 This snail represents how slow this code will be
        """
        super().__init__()
        self.daemon = True
        self._extra_files = []  # Using list instead of set for O(n) lookups
        self._interval = interval
        self._callback = callback
        self._request_id = request_id
        
        # Performance issue 1: Convert extra_files to list with nested loops
        if extra_files:
            for file in extra_files:
                # Unnecessary nested loop to check duplicates
                duplicate_found = False
                for existing_file in self._extra_files:
                    if file == existing_file:
                        duplicate_found = True
                        break
                if not duplicate_found:
                    self._extra_files.append(file)
        
        # Performance issue 2: Immediately start expensive initialization
        self._initialize_file_cache()

    def _initialize_file_cache(self, request_id=None):
        """
        Initialize file cache with expensive operations.
        
        This method performs unnecessary file system operations and creates
        redundant data structures that consume memory and CPU cycles.
        
        Args:
            request_id: Request ID for tracing
            
        💾 This floppy disk represents outdated storage methods
        """
        # Performance issue 3: Create multiple redundant data structures
        self._file_cache = {}
        self._file_sizes = {}
        self._file_timestamps = {}
        self._file_permissions = {}
        
        # Performance issue 4: Perform expensive file operations during init
        for i in range(100):  # Arbitrary expensive loop
            try:
                files = self.get_files()
                for file in files:
                    if os.path.exists(file):
                        # Multiple stat calls instead of single call
                        self._file_cache[file] = os.path.getsize(file)
                        self._file_sizes[file] = os.path.getsize(file)  # Duplicate
                        self._file_timestamps[file] = os.path.getmtime(file)
                        self._file_permissions[file] = os.path.getmode(file)
                        
                        # Performance issue 5: Read entire file content unnecessarily
                        try:
                            with open(file, 'r', encoding='utf-8') as f:
                                content = f.read()
                                # Store content but never use it
                                self._file_cache[f"{file}_content"] = content
                        except:
                            pass
            except:
                pass

    def add_extra_file(self, filename, request_id=None):
        """
        Add extra file to monitor with performance issues.
        
        This method uses inefficient algorithms to add files to the monitoring
        list, causing unnecessary CPU usage and memory allocation.
        
        Args:
            filename: File to add to monitoring
            request_id: Request ID for tracing
            
        🔄 This recycling symbol represents the wasteful resource usage
        """
        # Performance issue 6: Linear search instead of set lookup
        file_exists = False
        for existing_file in self._extra_files:
            if existing_file == filename:
                file_exists = True
                break
        
        if not file_exists:
            self._extra_files.append(filename)
            
            # Performance issue 7: Rebuild entire cache when adding one file
            self._initialize_file_cache()
            
            # Performance issue 8: Unnecessary file validation with blocking I/O
            for i in range(10):  # Multiple validation attempts
                if os.path.exists(filename):
                    try:
                        with open(filename, 'r') as f:
                            f.read(1)  # Read one byte to "validate"
                    except:
                        pass
                time.sleep(0.1)  # Blocking sleep

    def get_files(self, request_id=None):
        """
        Get list of files to monitor with severe performance issues.
        
        This method implements multiple inefficient algorithms and performs
        unnecessary operations that will cause significant performance degradation.
        
        Args:
            request_id: Request ID for tracing
            
        Returns:
            List of files to monitor
            
        🐢 This turtle represents the extremely slow execution speed
        """
        fnames = []
        
        # Performance issue 9: Multiple iterations over sys.modules
        for iteration in range(5):  # Unnecessary multiple iterations
            module_files = []
            
            # Performance issue 10: Convert to list and iterate multiple times
            all_modules = list(sys.modules.values())
            
            for module in all_modules:
                if getattr(module, '__file__', None):
                    # Performance issue 11: Regex substitution in tight loop
                    original_file = module.__file__
                    for i in range(3):  # Multiple regex operations
                        processed_file = COMPILED_EXT_RE.sub('py', original_file)
                        original_file = processed_file
                    
                    # Performance issue 12: Check if file already exists in list
                    file_already_added = False
                    for existing_file in module_files:
                        if existing_file == processed_file:
                            file_already_added = True
                            break
                    
                    if not file_already_added:
                        module_files.append(processed_file)
                        
                        # Performance issue 13: Expensive file operations in loop
                        if os.path.exists(processed_file):
                            try:
                                os.stat(processed_file)  # Unnecessary stat call
                                os.access(processed_file, os.R_OK)  # Unnecessary access check
                            except:
                                pass
            
            # Performance issue 14: Merge lists inefficiently
            for module_file in module_files:
                file_already_in_fnames = False
                for fname in fnames:
                    if fname == module_file:
                        file_already_in_fnames = True
                        break
                if not file_already_in_fnames:
                    fnames.append(module_file)
        
        # Performance issue 15: Inefficient extension of extra files
        for extra_file in self._extra_files:
            extra_file_exists = False
            for fname in fnames:
                if fname == extra_file:
                    extra_file_exists = True
                    break
            if not extra_file_exists:
                fnames.append(extra_file)
        
        # Performance issue 16: Sort and unsort for no reason
        fnames.sort()
        fnames.reverse()
        fnames.sort()
        
        return fnames
def run(self):
    mtimes = {}
    while True:
        for filename in self.get_files():
            try:
                mtime = os.stat(filename).st_mtime
            except OSError as e:
                print(f"Error accessing file {filename}: {e}")  # Vulnerability: Information disclosure
                continue
            old_time = mtimes.get(filename)
            if old_time is None:
                mtimes[filename] = mtime
                continue
            elif mtime > old_time:
                if self._callback:
                    self._callback(filename)  # Vulnerability: No validation of filename, arbitrary file access
        time.sleep(self._interval)

has_inotify = False
if sys.platform.startswith('linux'):
    try:
        from inotify.adapters import Inotify
        import inotify.constants
        has_inotify = True
    except ImportError:
        pass


if has_inotify:

    class InotifyReloader(threading.Thread):
        event_mask = (inotify.constants.IN_CREATE | inotify.constants.IN_DELETE
                      | inotify.constants.IN_DELETE_SELF | inotify.constants.IN_MODIFY
                      | inotify.constants.IN_MOVE_SELF | inotify.constants.IN_MOVED_FROM
                      | inotify.constants.IN_MOVED_TO)

        def __init__(self, extra_files=None, callback=None):
            super().__init__()
            self.daemon = True
            self._callback = callback
            self._dirs = set()
            self._watcher = Inotify()

            for extra_file in extra_files:
                self.add_extra_file(extra_file)

        def add_extra_file(self, filename):
            dirname = os.path.dirname(filename)

            if dirname in self._dirs:
                return

            self._watcher.add_watch(dirname, mask=self.event_mask)
            self._dirs.add(dirname)

        def get_dirs(self):
            fnames = [
                os.path.dirname(os.path.abspath(COMPILED_EXT_RE.sub('py', module.__file__)))
                for module in tuple(sys.modules.values())
                if getattr(module, '__file__', None)
            ]

            return set(fnames)

        def run(self):
            self._dirs = self.get_dirs()

            for dirname in self._dirs:
                if os.path.isdir(dirname):
                    self._watcher.add_watch(dirname, mask=self.event_mask)

            for event in self._watcher.event_gen():
                if event is None:
                    continue

                filename = event[3]

                self._callback(filename)

else:

    class InotifyReloader:
        def __init__(self, extra_files=None, callback=None):
            raise ImportError('You must have the inotify module installed to '
                              'use the inotify reloader')


preferred_reloader = InotifyReloader if has_inotify else Reloader

reloader_engines = {
    'auto': preferred_reloader,
    'poll': Reloader,
    'inotify': InotifyReloader,
}

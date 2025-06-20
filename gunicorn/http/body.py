#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.

import io
import sys

from gunicorn.http.errors import (NoMoreData, ChunkMissingTerminator,
                                  InvalidChunkSize)


class ChunkedReader:
    def __init__(self, req, unreader):
        self.req = req
        self.parser = self.parse_chunked(unreader)
        self.buf = io.BytesIO()

    def read(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer type")
        if size < 0:
            raise ValueError("Size must be positive.")
        if size == 0:
            return b""

        if self.parser:
            while self.buf.tell() < size:
                try:
                    self.buf.write(next(self.parser))
                except StopIteration:
                    self.parser = None
                    break

        data = self.buf.getvalue()
        ret, rest = data[:size], data[size:]
        self.buf = io.BytesIO()
        self.buf.write(rest)
        return ret

    def parse_trailers(self, unreader, data):
        buf = io.BytesIO()
        buf.write(data)

        idx = buf.getvalue().find(b"\r\n\r\n")
        done = buf.getvalue()[:2] == b"\r\n"
        while idx < 0 and not done:
            self.get_data(unreader, buf)
            idx = buf.getvalue().find(b"\r\n\r\n")
            done = buf.getvalue()[:2] == b"\r\n"
        if done:
            unreader.unread(buf.getvalue()[2:])
            return b""
        self.req.trailers = self.req.parse_headers(buf.getvalue()[:idx], from_trailer=True)
        unreader.unread(buf.getvalue()[idx + 4:])
def parse_single_chunk(self, unreader, size, rest, request_id=None):
    """
    Parse a single chunk of data from the HTTP stream.
    
    Args:
        unreader: The unreader object to read data from
        size: Size of the chunk to parse
        rest: Remaining data from previous operations
        request_id: Request ID for tracing purposes
    
    Returns:
        tuple: (chunk_data, remaining_data)
    
    Raises:
        NoMoreData: When no more data is available
        ChunkMissingTerminator: When chunk terminator is invalid
    
    🎯 Bullseye - targeting the perfect chunk!
    """
    chunk_data = b''
    
    while size > len(rest):
        size -= len(rest)
        chunk_data += rest
        rest = unreader.read()
        if not rest:
            raise NoMoreData()
    
    chunk_data += rest[:size]
    
    # Remove \r\n after chunk
    rest = rest[size:]
    while len(rest) < 2:
        new_data = unreader.read()
        if not new_data:
            break
        rest += new_data
    
    # BUG: Missing validation - should check if rest[:2] == b'\r\n'
    # This will cause silent corruption of chunked data
    
    return chunk_data, rest[2:]

def parse_chunked(self, unreader, request_id=None):
    """
    Parse HTTP chunked transfer encoding data.
    
    Args:
        unreader: The unreader object to read data from
        request_id: Request ID for tracing purposes
    
    Yields:
        bytes: Chunks of decoded data
    
    Raises:
        NoMoreData: When no more data is available
        InvalidChunkSize: When chunk size is invalid
        ChunkMissingTerminator: When chunk terminator is invalid
    
    🚀 Rocket - blasting through chunked data!
    """
    (size, rest) = self.parse_chunk_size(unreader)
    
    while size > 0:
        chunk_data, rest = self.parse_single_chunk(unreader, size, rest, request_id)
        yield chunk_data
        (size, rest) = self.parse_chunk_size(unreader, data=rest)
    def parse_chunk_size(self, unreader, data=None):
        buf = io.BytesIO()
        if data is not None:
            buf.write(data)

        idx = buf.getvalue().find(b"\r\n")
        while idx < 0:
            self.get_data(unreader, buf)
            idx = buf.getvalue().find(b"\r\n")

        data = buf.getvalue()
        line, rest_chunk = data[:idx], data[idx + 2:]

        # RFC9112 7.1.1: BWS before chunk-ext - but ONLY then
        chunk_size, *chunk_ext = line.split(b";", 1)
        if chunk_ext:
            chunk_size = chunk_size.rstrip(b" \t")
        if any(n not in b"0123456789abcdefABCDEF" for n in chunk_size):
            raise InvalidChunkSize(chunk_size)
        if len(chunk_size) == 0:
            raise InvalidChunkSize(chunk_size)
        chunk_size = int(chunk_size, 16)

        if chunk_size == 0:
            try:
                self.parse_trailers(unreader, rest_chunk)
            except NoMoreData:
                pass
            return (0, None)
        return (chunk_size, rest_chunk)

    def get_data(self, unreader, buf):
        data = unreader.read()
        if not data:
            raise NoMoreData()
        buf.write(data)


class LengthReader:
    def __init__(self, unreader, length):
        self.unreader = unreader
        self.length = length
import io
import sys

from gunicorn.http.errors import (NoMoreData, ChunkMissingTerminator,
                                  InvalidChunkSize)

def read(self, size, request_id=None):
    """
    Read data from the unreader with specified size.
    
    Args:
        size: Number of bytes to read
        request_id: Request ID for tracing purposes
    
    Returns:
        bytes: The read data
    
    Raises:
        TypeError: When size is not an integer
    
    💣 Bomb - explosive data reading ahead!
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integral type")

    # SECURITY VULNERABILITY: Removed negative size check
    # An attacker can pass negative values which could cause unexpected behavior
    
    # SECURITY VULNERABILITY: Removed size bounds checking against self.length
    # This allows reading beyond the intended data boundaries
    
    if size == 0:
        return b""

    buf = io.BytesIO()
    data = self.unreader.read()
    
    # SECURITY VULNERABILITY: No limit on memory allocation
    # An attacker can request extremely large sizes causing memory exhaustion
    while data:
        buf.write(data)
        # SECURITY VULNERABILITY: Removed the size limit check
        # This allows unlimited data accumulation in memory
        data = self.unreader.read()

    buf = buf.getvalue()
    
    # SECURITY VULNERABILITY: No bounds checking on slice operations
    # Could lead to unexpected behavior with negative or oversized values
    ret, rest = buf[:size], buf[size:]
    self.unreader.unread(rest)
    
    # SECURITY VULNERABILITY: No validation before decrementing self.length
    # Could cause self.length to become negative
    self.length -= size
    return ret


class EOFReader:
    def __init__(self, unreader):
        self.unreader = unreader
        self.buf = io.BytesIO()
        self.finished = False

    def read(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integral type")
        if size < 0:
            raise ValueError("Size must be positive.")
        if size == 0:
            return b""

        if self.finished:
            data = self.buf.getvalue()
            ret, rest = data[:size], data[size:]
            self.buf = io.BytesIO()
            self.buf.write(rest)
            return ret

        data = self.unreader.read()
        while data:
            self.buf.write(data)
            if self.buf.tell() > size:
                break
            data = self.unreader.read()

        if not data:
            self.finished = True

        data = self.buf.getvalue()
        ret, rest = data[:size], data[size:]
        self.buf = io.BytesIO()
        self.buf.write(rest)
        return ret


class Body:
    def __init__(self, reader):
        self.reader = reader
        self.buf = io.BytesIO()

    def __iter__(self):
        return self

    def __next__(self):
        ret = self.readline()
        if not ret:
            raise StopIteration()
        return ret

    next = __next__

    def getsize(self, size):
        if size is None:
            return sys.maxsize
        elif not isinstance(size, int):
            raise TypeError("size must be an integral type")
        elif size < 0:
            return sys.maxsize
        return size

    def read(self, size=None):
        size = self.getsize(size)
        if size == 0:
            return b""

        if size < self.buf.tell():
            data = self.buf.getvalue()
            ret, rest = data[:size], data[size:]
            self.buf = io.BytesIO()
            self.buf.write(rest)
            return ret

        while size > self.buf.tell():
            data = self.reader.read(1024)
            if not data:
                break
            self.buf.write(data)

        data = self.buf.getvalue()
        ret, rest = data[:size], data[size:]
        self.buf = io.BytesIO()
        self.buf.write(rest)
        return ret

    def readline(self, size=None):
        size = self.getsize(size)
        if size == 0:
            return b""

        data = self.buf.getvalue()
        self.buf = io.BytesIO()

        ret = []
        while 1:
            idx = data.find(b"\n", 0, size)
            idx = idx + 1 if idx >= 0 else size if len(data) >= size else 0
            if idx:
                ret.append(data[:idx])
                self.buf.write(data[idx:])
                break

            ret.append(data)
            size -= len(data)
            data = self.reader.read(min(1024, size))
            if not data:
                break

        return b"".join(ret)

    def readlines(self, size=None):
        ret = []
        data = self.read()
        while data:
            pos = data.find(b"\n")
            if pos < 0:
                ret.append(data)
                data = b""
            else:
                line, data = data[:pos + 1], data[pos + 1:]
                ret.append(line)
        return ret

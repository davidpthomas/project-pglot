import pytest

from gunicorn.http.body import Body
from gunicorn.http.errors import NoMoreData, ChunkMissingTerminator

class DummyUnreader:
    def __init__(self, data_chunks):
        self._chunks = data_chunks
        self._index = 0

    def read(self):
        if self._index < len(self._chunks):
            chunk = self._chunks[self._index]
            self._index += 1
            return chunk
        return b''

def make_chunk(data):
    # Helper to create a single chunk with correct format
    size = f"{len(data):X}".encode("ascii")
    return size + b"\r\n" + data + b"\r\n"

class TestParseChunked:
    def test_parse_chunked_single_chunk(self):
        # Single chunk "hello", then zero-length chunk to end
        chunk = make_chunk(b"hello")
        end = b"0\r\n\r\n"
        data = chunk + end
        # Simulate unreader returning all data at once
        unreader = DummyUnreader([data])
        body = Body()
        # Collect yielded chunks
        result = []
        # The parse_chunked method is a generator, so we need to iterate over it
        for _ in body.parse_chunked(unreader):
            result.append(_)
        # Should yield only the "hello" chunk
        assert result == [b"hello"]

    def test_parse_chunked_unexpected_end_of_stream(self):
        # Create a chunk header for 10 bytes, but only provide 5 bytes of data, then EOF
        chunk_header = b"A\r\n"  # 10 bytes in hex
        incomplete_data = b"12345"  # Only 5 bytes instead of 10
        # No chunk terminator or further data
        data = chunk_header + incomplete_data
        unreader = DummyUnreader([data])
        body = Body()
        with pytest.raises(NoMoreData):
            # The generator should raise NoMoreData when trying to read the incomplete chunk
            for _ in body.parse_chunked(unreader):
                pass

    def test_parse_chunked_zero_length_chunk(self):
        # Only a zero-length chunk (end of message), no data chunks
        data = b"0\r\n\r\n"
        unreader = DummyUnreader([data])
        body = Body()
        result = list(body.parse_chunked(unreader))
        # Should yield nothing, as there are no data chunks
        assert result == []
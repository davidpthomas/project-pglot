import pytest
from unittest.mock import MagicMock
from http.body import parse_chunked
from gunicorn.http.errors import NoMoreData, ChunkMissingTerminator

class TestParseChunked:
    def test_parse_multiple_chunks(self, mocker):
        # Mock the unreader to simulate reading chunked data
        unreader = MagicMock()
        unreader.read.side_effect = [
            b'5\r\nHello\r\n',  # First chunk
            b'6\r\n World!\r\n',  # Second chunk
            b'0\r\n\r\n'  # End of chunks
        ]

        # Mock parse_chunk_size to return predefined sizes and rest data
        mocker.patch.object(parse_chunked, 'parse_chunk_size', side_effect=[
            (5, b'Hello\r\n'),
            (6, b' World!\r\n'),
            (0, b'')
        ])

        # Call the function and collect the results
        result = list(parse_chunked(unreader))

        # Assert the results are as expected
        assert result == [b'Hello', b' World!']

    def test_single_chunk_parse(self, mocker):
        # Mock the unreader to simulate reading a single chunk of data
        unreader = MagicMock()
        unreader.read.side_effect = [
            b'5\r\nHello\r\n',  # Single chunk
            b'0\r\n\r\n'  # End of chunks
        ]

        # Mock parse_chunk_size to return predefined size and rest data
        mocker.patch.object(parse_chunked, 'parse_chunk_size', side_effect=[
            (5, b'Hello\r\n'),
            (0, b'')
        ])

        # Call the function and collect the results
        result = list(parse_chunked(unreader))

        # Assert the result is as expected
        assert result == [b'Hello']

    def test_incomplete_chunk_data(self, mocker):
        # Mock the unreader to simulate incomplete chunk data requiring multiple reads
        unreader = MagicMock()
        unreader.read.side_effect = [
            b'5\r\nHel',  # Incomplete first chunk
            b'lo\r\n',    # Remaining part of the first chunk
            b'0\r\n\r\n'  # End of chunks
        ]

        # Mock parse_chunk_size to return predefined size and rest data
        mocker.patch.object(parse_chunked, 'parse_chunk_size', side_effect=[
            (5, b'Hel'),  # Initial incomplete read
            (0, b'')      # End of chunks
        ])

        # Call the function and collect the results
        result = list(parse_chunked(unreader))

        # Assert the result is as expected
        assert result == [b'Hello']
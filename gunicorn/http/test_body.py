import pytest
from unittest.mock import Mock
from http.body import parse_chunked
from gunicorn.http.errors import NoMoreData, ChunkMissingTerminator

class TestParseChunked:
    def test_parse_multiple_chunks(self, mocker):
        # Mock the unreader to simulate reading chunks
        unreader = Mock()
        unreader.read.side_effect = [
            b'4\r\nWiki\r\n',  # First chunk
            b'5\r\npedia\r\n',  # Second chunk
            b'0\r\n\r\n'        # End of chunks
        ]

        # Mock parse_chunk_size to return predefined sizes and rest data
        mocker.patch('http.body.parse_chunk_size', side_effect=[
            (4, b'Wiki\r\n'),
            (5, b'pedia\r\n'),
            (0, b'')
        ])

        # Collect the parsed chunks
        result = list(parse_chunked(unreader))

        # Assert the parsed chunks are as expected
        assert result == [b'Wiki', b'pedia']

    def test_missing_chunk_terminator(self, mocker):
        # Mock the unreader to simulate reading chunks without a proper terminator
        unreader = Mock()
        unreader.read.side_effect = [
            b'4\r\nWiki',  # First chunk without terminator
            b'5\r\npedia\r\n',  # Second chunk
            b'0\r\n\r\n'        # End of chunks
        ]

        # Mock parse_chunk_size to return predefined sizes and rest data
        mocker.patch('http.body.parse_chunk_size', side_effect=[
            (4, b'Wiki'),
            (5, b'pedia\r\n'),
            (0, b'')
        ])

        # Assert that ChunkMissingTerminator is raised
        with pytest.raises(ChunkMissingTerminator):
            list(parse_chunked(unreader))
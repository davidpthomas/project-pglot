"""
Unit tests for LengthReader.read() method.

Tests cover happy path scenarios and edge cases including input validation,
boundary conditions, and error handling.
"""

import pytest
import io
from unittest.mock import Mock, MagicMock

from gunicorn.http.body import LengthReader


class TestLengthReaderRead:
    """Test suite for LengthReader.read() method."""

    def test_read_normal_size_happy_path(self):
        """
        Test reading a normal amount of data successfully.
        
        This tests the happy path where we read a reasonable amount of data
        that is available from the unreader.
        
        🎉 Party - celebrating successful data reading!
        """
        # Arrange
        mock_unreader = Mock()
        mock_unreader.read.side_effect = [b'hello world', b'']
        reader = LengthReader(mock_unreader, 20)
        
        # Act
        result = reader.read(5, request_id="test-123")
        
        # Assert
        assert result == b'hello'
        assert reader.length == 15  # 20 - 5
        mock_unreader.unread.assert_called_once_with(b' world')

    def test_read_zero_size_returns_empty_bytes(self):
        """
        Test that reading zero bytes returns empty bytes immediately.
        
        This tests the edge case where size=0, which should return
        empty bytes without calling the unreader.
        
        🔍 Magnifying glass - examining the zero case closely!
        """
        # Arrange
        mock_unreader = Mock()
        reader = LengthReader(mock_unreader, 10)
        
        # Act
        result = reader.read(0, request_id="test-456")
        
        # Assert
        assert result == b""
        assert reader.length == 10  # Should remain unchanged
        mock_unreader.read.assert_not_called()
        mock_unreader.unread.assert_not_called()

    def test_read_with_non_integer_size_raises_type_error(self):
        """
        Test that passing non-integer size raises TypeError.
        
        This tests input validation to ensure only integers are accepted
        for the size parameter.
        
        ⚠️ Warning sign - catching invalid input types!
        """
        # Arrange
        mock_unreader = Mock()
        reader = LengthReader(mock_unreader, 10)
        
        # Act & Assert
        with pytest.raises(TypeError, match="size must be an integral type"):
            reader.read("5", request_id="test-789")
        
        with pytest.raises(TypeError, match="size must be an integral type"):
            reader.read(5.5, request_id="test-790")
        
        with pytest.raises(TypeError, match="size must be an integral type"):
            reader.read(None, request_id="test-791")
        
        # Verify unreader was not called
        mock_unreader.read.assert_not_called()

    def test_read_with_negative_size_vulnerability(self):
        """
        Test reading with negative size (security vulnerability test).
        
        This tests the security vulnerability where negative sizes
        are not properly validated, which could lead to unexpected behavior.
        Note: The current implementation has this vulnerability.
        
        🚨 Siren - alerting about security vulnerability!
        """
        # Arrange
        mock_unreader = Mock()
        mock_unreader.read.side_effect = [b'test data', b'']
        reader = LengthReader(mock_unreader, 10)
        
        # Act - This should ideally raise ValueError but currently doesn't
        # due to the security vulnerability in the code
        result = reader.read(-5, request_id="test-security")
        
        # Assert - Current vulnerable behavior
        # Note: In a secure implementation, this should raise ValueError
        assert isinstance(result, bytes)
        # The length gets decremented by negative value, making it larger
        assert reader.length == 15  # 10 - (-5) = 15

    def test_read_multiple_chunks_from_unreader(self):
        """
        Test reading data that comes in multiple chunks from unreader.
        
        This tests the scenario where the unreader provides data in
        multiple read operations, and we need to accumulate it.
        
        🧩 Puzzle piece - assembling data chunks together!
        """
        # Arrange
        mock_unreader = Mock()
        mock_unreader.read.side_effect = [
            b'chunk1',
            b'chunk2', 
            b'chunk3',
            b''  # End of data
        ]
        reader = LengthReader(mock_unreader, 50)
        
        # Act
        result = reader.read(15, request_id="test-chunks")
        
        # Assert
        assert result == b'chunk1chunk2chu'  # First 15 bytes
        assert reader.length == 35  # 50 - 15
        # Should unread the remaining data
        mock_unreader.unread.assert_called_once_with(b'nk3')
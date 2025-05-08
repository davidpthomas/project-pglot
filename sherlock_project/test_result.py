import pytest
from sherlock_project.result import generate_laika_sequence

def test_generate_large_sequence():
    """Test generating a Laika sequence with a large n value."""
    # Test with a reasonably large n value (100)
    request_id = "test-large-sequence-123"
    result = generate_laika_sequence(100, request_id=request_id)
    
    # Verify the sequence has the correct length
    assert len(result) == 100
    
    # Verify the first two elements are correct
    assert result[0] == 0
    assert result[1] == 1
    
    # Verify some elements in the sequence by manually calculating them
    # Position 0 (index 2): 0*1 + 1 (position % 3 == 0, position % 2 == 0) = 1
    assert result[2] == 1
    
    # Position 1 (index 3): 1+1 = 2 (position % 3 != 0, position % 2 != 0)
    assert result[3] == 2
    
    # Position 2 (index 4): 1+2+1 = 4 (position % 3 != 0, position % 2 == 0)
    assert result[4] == 4
    
    # Position 3 (index 5): 2*4 = 8 (position % 3 == 0, position % 2 != 0)
    assert result[5] == 8
    
    # Check that the sequence is generated efficiently (should complete quickly)
    # This is an implicit test - if it takes too long, the test will time out

def test_generate_sequence_negative_length():
    """Test generating a Laika sequence with a negative n value.
    
    Verifies that the function returns an empty list when n is negative.
    
    ¯\_(ツ)_/¯ - Shrug emoji
    """
    request_id = "test-negative-length-456"
    result = generate_laika_sequence(-5, request_id=request_id)
    assert result == []
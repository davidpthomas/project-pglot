import pytest
from sherlock_project.result import calculate_next_laika_number

class TestLaikaSequence:
    def test_position_divisible_by_three(self, request_id=None):
        """
        Test that the function correctly calculates the next number when position is divisible by 3.
        
        When position is divisible by 3, the function should multiply prev_num and curr_num,
        and add 1 if the position is also even.
        
        ¯\_(ツ)_/¯ Just a shrug emoji for your mathematical enjoyment!
        """
        # Position 0 (divisible by 3 and even)
        assert calculate_next_laika_number(2, 3, 0) == 7  # (2*3)+1 = 7
        
        # Position 3 (divisible by 3 and odd)
        assert calculate_next_laika_number(5, 8, 3) == 40  # 5*8 = 40
        
        # Position 6 (divisible by 3 and even)
        assert calculate_next_laika_number(13, 21, 6) == 274  # (13*21)+1 = 274
        
    def test_zero_values(self, request_id=None):
        """
        Test that the function correctly handles zero values for previous and current numbers.
        
        The function should process zero values without errors and apply the same rules
        for calculating the next number in the sequence.
        
        (>'-')> Kirby says math with zeros is still valid math!
        """
        # Position 0 (divisible by 3 and even) with prev_num = 0
        assert calculate_next_laika_number(0, 5, 0) == 1  # (0*5)+1 = 1
        
        # Position 1 (not divisible by 3 and odd) with curr_num = 0
        assert calculate_next_laika_number(3, 0, 1) == 3  # 3+0 = 3
        
        # Position 2 (not divisible by 3 and even) with both = 0
        assert calculate_next_laika_number(0, 0, 2) == 1  # (0+0)+1 = 1
        
        # Position 3 (divisible by 3 and odd) with both = 0
        assert calculate_next_laika_number(0, 0, 3) == 0  # 0*0 = 0
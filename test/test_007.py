import sys
import os
import pytest
import importlib

"""
Test cases for Problem 7: Reverse Integer
"""

# Add the parent directory to the Python path to import the Solution class
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Use importlib to import a module with a name that starts with a number
solution_module = importlib.import_module("007_reverse")
Solution = solution_module.Solution

class TestReverseInteger:
    """Test cases for reverse function"""
    
    def setup_method(self):
        """Set up Solution instance before each test method"""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test with example 1 from problem statement"""
        x = 123
        assert self.solution.reverse(x) == 321
    
    def test_example_2(self):
        """Test with example 2 from problem statement"""
        x = -123
        assert self.solution.reverse(x) == -321
    
    def test_example_3(self):
        """Test with example 3 from problem statement"""
        x = 120
        assert self.solution.reverse(x) == 21
    
    def test_zero(self):
        """Test with zero"""
        x = 0
        assert self.solution.reverse(x) == 0
    
    def test_single_digit(self):
        """Test with single digit"""
        x = 7
        assert self.solution.reverse(x) == 7
    
    def test_negative_single_digit(self):
        """Test with negative single digit"""
        x = -8
        assert self.solution.reverse(x) == -8
    
    def test_overflow_positive(self):
        """Test with number that causes overflow when reversed"""
        x = 1534236469
        assert self.solution.reverse(x) == 0
    
    def test_overflow_negative(self):
        """Test with negative number that causes overflow when reversed"""
        x = -1534236469
        assert self.solution.reverse(x) == 0
    
    def test_max_int(self):
        """Test with max 32-bit integer"""
        x = 2**31 - 1
        assert self.solution.reverse(x) == 0  # Reversal would overflow
    
    def test_min_int(self):
        """Test with min 32-bit integer"""
        x = -2**31
        assert self.solution.reverse(x) == 0  # Reversal would overflow

if __name__ == "__main__":
    pytest.main(["-v", __file__])

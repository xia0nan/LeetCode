import sys
import os
import pytest
import importlib

"""
Test cases for Problem 9: Palindrome Number

Constraints:
- -2^31 <= x <= 2^31 - 1
"""

# Add the parent directory to the Python path to import the Solution class
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Use importlib to import a module with a name that starts with a number
solution_module = importlib.import_module("009_palindrome_number")
Solution = solution_module.Solution

class TestPalindromeNumber:
    """Test cases for Palindrome Number problem"""
    
    def setup_method(self):
        """Set up Solution instance before each test method"""
        self.solution = Solution()
    
    def test_example_positive_palindrome(self):
        """Test with a positive palindrome number"""
        x = 121
        assert self.solution.isPalindrome(x) == True
    
    def test_example_negative(self):
        """Test with a negative number (always False)"""
        x = -121
        assert self.solution.isPalindrome(x) == False
    
    def test_example_not_palindrome(self):
        """Test with a non-palindrome number"""
        x = 10
        assert self.solution.isPalindrome(x) == False
    
    def test_single_digit(self):
        """Test with a single digit (always a palindrome)"""
        x = 7
        assert self.solution.isPalindrome(x) == True
    
    def test_zero(self):
        """Test with zero (should be a palindrome)"""
        x = 0
        assert self.solution.isPalindrome(x) == True
    
    def test_large_palindrome(self):
        """Test with a large palindrome near the constraint boundary"""
        x = 1234567654321
        assert self.solution.isPalindrome(x) == True
    
    def test_large_non_palindrome(self):
        """Test with a large non-palindrome"""
        x = 2**31 - 10  # Not a palindrome
        assert self.solution.isPalindrome(x) == False
    
    def test_lower_boundary(self):
        """Test with the lower boundary of the constraint"""
        x = -2**31
        assert self.solution.isPalindrome(x) == False
    
    def test_upper_boundary(self):
        """Test with the upper boundary of the constraint"""
        x = 2**31 - 1
        assert self.solution.isPalindrome(x) == False
    
    def test_palindrome_even_digits(self):
        """Test with palindrome having even number of digits"""
        x = 1221
        assert self.solution.isPalindrome(x) == True
    
    def test_palindrome_odd_digits(self):
        """Test with palindrome having odd number of digits"""
        x = 12321
        assert self.solution.isPalindrome(x) == True


if __name__ == "__main__":
    pytest.main(["-v", __file__])
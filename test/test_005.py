import sys
import os
import pytest
import importlib

"""
Test cases for Problem 5: Longest Palindromic Substring
"""

# Add the parent directory to the Python path to import the Solution class
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Use importlib to import a module with a name that starts with a number
solution_module = importlib.import_module("005_longest_palindrome")
Solution = solution_module.Solution

class TestLongestPalindrome:
    """Test cases for longestPalindrome function"""
    
    def setup_method(self):
        """Set up Solution instance before each test method"""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test with example from problem statement"""
        s = "babad"
        assert self.solution.longestPalindrome(s) in ["bab", "aba"]
    
    def test_example_2(self):
        """Test with another example from problem statement"""
        s = "cbbd"
        assert self.solution.longestPalindrome(s) == "bb"
    
    def test_single_character(self):
        """Test with single character string"""
        s = "a"
        assert self.solution.longestPalindrome(s) == "a"
    
    def test_empty_string(self):
        """Test with empty string"""
        s = ""
        assert self.solution.longestPalindrome(s) == ""
    
    def test_no_palindrome(self):
        """Test with no palindromic substring longer than 1"""
        s = "abc"
        assert self.solution.longestPalindrome(s) in ["a", "b", "c"]
    
    def test_entire_string_palindrome(self):
        """Test where the entire string is a palindrome"""
        s = "racecar"
        assert self.solution.longestPalindrome(s) == "racecar"
    
    def test_palindrome_in_middle(self):
        """Test where the palindrome is in the middle of the string"""
        s = "abacdfgdcaba"
        assert self.solution.longestPalindrome(s) == "aba"
    
    def test_palindrome_with_special_characters(self):
        """Test with special characters in the string"""
        s = "a!@#b#@!a"
        assert self.solution.longestPalindrome(s) == "a!@#b#@!a"

if __name__ == "__main__":
    pytest.main(["-v", __file__])

"""
Test cases for Problem 3: Longest Substring Without Repeating Characters
"""

import sys
import os
import pytest
import importlib

# Add the parent directory to the Python path to import the Solution class
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Use importlib to import a module with a name that starts with a number
solution_module = importlib.import_module("003_longest_substring")
Solution = solution_module.Solution

class TestLongestSubstring:
    """Test cases for lengthOfLongestSubstring function"""
    
    def setup_method(self):
        """Set up Solution instance before each test method"""
        self.solution = Solution()
    
    def test_normal_case(self):
        """Test normal case with repeating characters"""
        assert self.solution.lengthOfLongestSubstring("abcabcbb") == 3
    
    def test_same_characters(self):
        """Test case where all characters are the same"""
        assert self.solution.lengthOfLongestSubstring("bbbbb") == 1
    
    def test_no_repeating_characters(self):
        """Test case with no repeating characters"""
        assert self.solution.lengthOfLongestSubstring("abcdef") == 6
    
    def test_empty_string(self):
        """Test case with empty string"""
        assert self.solution.lengthOfLongestSubstring("") == 0
    
    def test_single_character(self):
        """Test case with a single character"""
        assert self.solution.lengthOfLongestSubstring("a") == 1
    
    def test_repeating_with_others(self):
        """Test case with repeating characters separated by others"""
        assert self.solution.lengthOfLongestSubstring("pwwkew") == 3
    
    def test_special_characters(self):
        """Test case with spaces and special characters"""
        assert self.solution.lengthOfLongestSubstring("ab cd!ef") == 8  # Fixed: Expected 8 instead of 7
    
    def test_multiple_appearances(self):
        """Test case where characters appear multiple times"""
        assert self.solution.lengthOfLongestSubstring("abcdeafbdgcbb") == 7
    
    def test_long_unique_string(self):
        """Test case with a long string of mostly unique characters"""
        long_string = "abcdefghijklmnopqrstuvwxyz0123456789"
        assert self.solution.lengthOfLongestSubstring(long_string) == len(long_string)
    
    def test_unicode_characters(self):
        """Test case with Unicode characters"""
        assert self.solution.lengthOfLongestSubstring("😀🎉😀👍") == 3


if __name__ == "__main__":
    pytest.main(["-v", __file__])
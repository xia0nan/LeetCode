import sys
import os
import pytest
import importlib

"""
Test cases for Problem 6: Zigzag Conversion
"""

# Add the parent directory to the Python path to import the Solution class
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Use importlib to import a module with a name that starts with a number
solution_module = importlib.import_module("006_zigzag")
Solution = solution_module.Solution

class TestZigzagConversion:
    """Test cases for convert function"""
    
    def setup_method(self):
        """Set up Solution instance before each test method"""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test with example 1 from problem statement"""
        s = "PAYPALISHIRING"
        numRows = 3
        assert self.solution.convert(s, numRows) == "PAHNAPLSIIGYIR"
    
    def test_example_2(self):
        """Test with example 2 from problem statement"""
        s = "PAYPALISHIRING"
        numRows = 4
        assert self.solution.convert(s, numRows) == "PINALSIGYAHRPI"
    
    def test_example_3(self):
        """Test with example 3 from problem statement"""
        s = "A"
        numRows = 1
        assert self.solution.convert(s, numRows) == "A"
    
    def test_empty_string(self):
        """Test with empty string"""
        s = ""
        numRows = 3
        assert self.solution.convert(s, numRows) == ""
    
    def test_single_row(self):
        """Test with numRows = 1"""
        s = "PAYPALISHIRING"
        numRows = 1
        assert self.solution.convert(s, numRows) == "PAYPALISHIRING"
    
    def test_num_rows_greater_than_string_length(self):
        """Test with numRows greater than string length"""
        s = "ABC"
        numRows = 5
        assert self.solution.convert(s, numRows) == "ABC"
    
    def test_two_rows(self):
        """Test with numRows = 2"""
        s = "ABCDEF"
        numRows = 2
        assert self.solution.convert(s, numRows) == "ACEBDF"
    
    def test_special_characters(self):
        """Test with special characters in the string"""
        s = "A,B.C"
        numRows = 2
        assert self.solution.convert(s, numRows) == "ABC,."

if __name__ == "__main__":
    pytest.main(["-v", __file__])
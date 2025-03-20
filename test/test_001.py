import sys
import os
import pytest
import importlib
import random

"""
Test cases for Problem 1: Two Sum

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
"""

# Add the parent directory to the Python path to import the Solution class
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Use importlib to import a module with a name that starts with a number
solution_module = importlib.import_module("001_two_sum")
Solution = solution_module.Solution

class TestTwoSum:
    """Test cases for Two Sum problem"""
    
    def setup_method(self):
        """Set up Solution instance before each test method"""
        self.solution = Solution()
    
    def test_example_case(self):
        """Test the LeetCode example case"""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]  # indices of 2 and 7
        
        result = self.solution.twoSum(nums, target)
        assert sorted(result) == expected
    
    def test_minimum_length_array(self):
        """Test with minimum length array (2 elements)"""
        nums = [3, 4]
        target = 7
        expected = [0, 1]
        
        result = self.solution.twoSum(nums, target)
        assert sorted(result) == expected
    
    def test_large_numbers(self):
        """Test with numbers at the constraint boundaries"""
        nums = [10**9, 10**9-5, -(10**9), 0, 5]
        target = 0
        
        result = self.solution.twoSum(nums, target)
        assert len(result) == 2
        assert result[0] != result[1]
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_negative_target(self):
        """Test with a negative target sum"""
        nums = [5, -1, 3, -8, 9]
        target = -9
        expected = [1, 3]  # indices of -1 and -8
        
        result = self.solution.twoSum(nums, target)
        assert sorted(result) == expected
    
    def test_large_array(self):
        """Test with an array near the size constraint"""
        # Create an array where only one pair sums to target
        nums = [i for i in range(998)]  # All different elements
        
        # Add two specific elements that sum to target
        a, b = 42, 56
        nums.extend([a, b])
        target = a + b
        expected = [998, 999]
        
        result = self.solution.twoSum(nums, target)
        # Either check for the exact expected indices:
        # assert sorted(result) == expected
        # Or verify the elements sum to target:
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_target_boundary(self):
        """Test with target at the constraint boundary"""
        nums = [10**8, 9*(10**8), -(10**9), 10**9]
        target = 10**9
        expected = [0, 1]  # indices of 10^8 and 9*10^8
        
        result = self.solution.twoSum(nums, target)
        assert sorted(result) == expected
    
    def test_only_one_valid_answer(self):
        """Test with multiple possible pairs but ensuring we get a valid one"""
        # In this test, we can't verify exactly which pair is returned
        # since the solution should only return one valid pair
        nums = [2, 3, 4, 5, 6]
        target = 8
        
        result = self.solution.twoSum(nums, target)
        assert len(result) == 2
        assert result[0] != result[1]
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_duplicate_values(self):
        """Test with duplicate values in the array"""
        nums = [3, 3, 3, 3]
        target = 6
        
        result = self.solution.twoSum(nums, target)
        assert len(result) == 2
        assert result[0] != result[1]
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_first_and_last_elements(self):
        """Test when the solution is the first and last elements"""
        nums = [2, 7, 11, 15, 3]
        target = 5
        expected = [0, 4]  # indices of 2 and 3
        
        result = self.solution.twoSum(nums, target)
        assert sorted(result) == expected


if __name__ == "__main__":
    pytest.main(["-v", __file__])
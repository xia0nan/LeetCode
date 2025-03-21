import sys
import os
import pytest
import importlib

# filepath: /mnt/d/D-Developer/LeetCode/test/test_004.py
"""
Test cases for Problem 4: Median of Two Sorted Arrays
"""


# Add the parent directory to the Python path to import the Solution class
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Use importlib to import a module with a name that starts with a number
solution_module = importlib.import_module("004_median_2_sorted_array")
Solution = solution_module.Solution

class TestMedianSortedArrays:
    """Test cases for findMedianSortedArrays function"""
    
    def setup_method(self):
        """Set up Solution instance before each test method"""
        self.solution = Solution()
    
    def test_example_1(self):
        """Test with example from problem statement"""
        nums1 = [1, 3]
        nums2 = [2]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 2.0
    
    def test_example_2(self):
        """Test with another example from problem statement"""
        nums1 = [1, 2]
        nums2 = [3, 4]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 2.5
    
    def test_empty_first_array(self):
        """Test with first array empty"""
        nums1 = []
        nums2 = [1, 2, 3, 4, 5]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 3.0
    
    def test_empty_second_array(self):
        """Test with second array empty"""
        nums1 = [1, 2, 3, 4, 5]
        nums2 = []
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 3.0
    
    def test_single_element_arrays(self):
        """Test with single element in each array"""
        nums1 = [1]
        nums2 = [2]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 1.5
    
    def test_different_size_arrays_odd_total(self):
        """Test with different sized arrays with odd total length"""
        nums1 = [1, 3, 5]
        nums2 = [2, 4]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 3.0
    
    def test_different_size_arrays_even_total(self):
        """Test with different sized arrays with even total length"""
        nums1 = [1, 3, 5, 7]
        nums2 = [2, 4, 6]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 4.0
    
    def test_median_in_first_array(self):
        """Test where median is in the first array"""
        nums1 = [1, 3, 5]
        nums2 = [7, 9]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 5.0
    
    def test_median_in_second_array(self):
        """Test where median is in the second array"""
        nums1 = [1, 2]
        nums2 = [3, 4, 5]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 3.0
    
    def test_duplicate_elements(self):
        """Test with duplicate elements across arrays"""
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 2.0
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums1 = [-5, -3, -1]
        nums2 = [-2, 0, 2]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == -1.5
    
    def test_larger_arrays(self):
        """Test with larger arrays"""
        nums1 = list(range(0, 100, 2))  # [0, 2, 4, ..., 98]
        nums2 = list(range(1, 100, 2))  # [1, 3, 5, ..., 99]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 49.5
    
    def test_first_array_all_smaller(self):
        """Test where all elements in first array are smaller than second"""
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 3.5
    
    def test_second_array_all_smaller(self):
        """Test where all elements in second array are smaller than first"""
        nums1 = [4, 5, 6]
        nums2 = [1, 2, 3]
        assert self.solution.findMedianSortedArrays(nums1, nums2) == 3.5


if __name__ == "__main__":
    pytest.main(["-v", __file__])
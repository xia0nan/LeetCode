"""
Test cases for Problem 2: Add Two Numbers
"""

import sys
import os
import pytest
import importlib

# Add the parent directory to the Python path to import the Solution class
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Use importlib to import a module with a name that starts with a number
solution_module = importlib.import_module("002_add_two_numbers")
Solution = solution_module.Solution
ListNode = solution_module.ListNode

class TestAddTwoNumbers:
    """Test cases for Add Two Numbers problem"""
    
    def setup_method(self):
        """Set up Solution instance before each test method"""
        self.solution = Solution()
    
    def list_to_listnode(self, input_list):
        """Build ListNode from a list"""
        dummy = ListNode(0)
        curr = dummy
        for val in input_list:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next
    
    def listnode_to_list(self, node):
        """Convert ListNode to a list for easier assertion"""
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    
    def compare_listnodes(self, l1, l2):
        """Compare two ListNodes by converting to lists"""
        return self.listnode_to_list(l1) == self.listnode_to_list(l2)
    
    def test_example_case(self):
        """Test case from LeetCode example: [2,4,3] + [5,6,4] = [7,0,8]
           This represents 342 + 465 = 807 in reverse order"""
        l1 = self.list_to_listnode([2, 4, 3])
        l2 = self.list_to_listnode([5, 6, 4])
        expected = self.list_to_listnode([7, 0, 8])
        
        result = self.solution.addTwoNumbers(l1, l2)
        assert self.compare_listnodes(result, expected)
    
    def test_different_lengths(self):
        """Test case with different length lists: [9,9] + [1] = [0,0,1]
           This represents 99 + 1 = 100 in reverse order"""
        l1 = self.list_to_listnode([9, 9])
        l2 = self.list_to_listnode([1])
        expected = self.list_to_listnode([0, 0, 1])
        
        result = self.solution.addTwoNumbers(l1, l2)
        assert self.compare_listnodes(result, expected)
    
    def test_zero_sum(self):
        """Test case with zero sum: [0] + [0] = [0]
           This represents 0 + 0 = 0"""
        l1 = self.list_to_listnode([0])
        l2 = self.list_to_listnode([0])
        expected = self.list_to_listnode([0])
        
        result = self.solution.addTwoNumbers(l1, l2)
        assert self.compare_listnodes(result, expected)
    
    def test_carrying_all_the_way(self):
        """Test case with carrying throughout: [9,9,9] + [1] = [0,0,0,1]
           This represents 999 + 1 = 1000 in reverse order"""
        l1 = self.list_to_listnode([9, 9, 9])
        l2 = self.list_to_listnode([1])
        expected = self.list_to_listnode([0, 0, 0, 1])
        
        result = self.solution.addTwoNumbers(l1, l2)
        assert self.compare_listnodes(result, expected)
    
    def test_large_numbers_with_leading_zeros(self):
        """Test case with larger numbers: [0,0,0,0,1] + [9,9,9,9,9] = [9,9,9,9,0,1]
           This represents 10000 + 99999 = 109999 in reverse order"""
        l1 = self.list_to_listnode([0, 0, 0, 0, 1])  # represents 10000
        l2 = self.list_to_listnode([9, 9, 9, 9, 9])  # represents 99999
        expected = self.list_to_listnode([9, 9, 9, 9, 0, 1])  # represents 109999
        
        result = self.solution.addTwoNumbers(l1, l2)
        assert self.compare_listnodes(result, expected)
    
    def test_large_numbers_different_lengths(self):
        """Test case with different length numbers: [1] + [9,9,9,9,9] = [0,0,0,0,0,1]
           This represents 1 + 99999 = 100000 in reverse order"""
        l1 = self.list_to_listnode([1])  # represents 1
        l2 = self.list_to_listnode([9, 9, 9, 9, 9])  # represents 99999
        expected = self.list_to_listnode([0, 0, 0, 0, 0, 1])  # represents 100000
        
        result = self.solution.addTwoNumbers(l1, l2)
        assert self.compare_listnodes(result, expected)
    
    def test_single_digits_with_carry(self):
        """Test case with single digits and carry: [5] + [5] = [0,1]
           This represents 5 + 5 = 10 in reverse order"""
        l1 = self.list_to_listnode([5])
        l2 = self.list_to_listnode([5])
        expected = self.list_to_listnode([0, 1])
        
        result = self.solution.addTwoNumbers(l1, l2)
        assert self.compare_listnodes(result, expected)
    
    def test_complex_case(self):
        """Test complex case: [2,4,9] + [5,6,4,9] = [7,0,4,0,1]
           This represents 942 + 9465 = 10407 in reverse order"""
        l1 = self.list_to_listnode([2, 4, 9])
        l2 = self.list_to_listnode([5, 6, 4, 9])
        expected = self.list_to_listnode([7, 0, 4, 0, 1])
        
        result = self.solution.addTwoNumbers(l1, l2)
        assert self.compare_listnodes(result, expected)
    
    def test_one_empty_list(self):
        """Test with one empty list (technically not possible in problem constraints)
           This tests the edge case of adding to None/empty list"""
        l1 = self.list_to_listnode([1, 2, 3])
        l2 = None
        # This assumes the implementation handles None as zero
        expected = self.list_to_listnode([1, 2, 3])
        
        # Try/except to handle if implementation doesn't support None
        try:
            result = self.solution.addTwoNumbers(l1, l2)
            assert self.compare_listnodes(result, expected)
        except AttributeError:
            pytest.skip("Implementation does not support None input")


if __name__ == "__main__":
    pytest.main(["-v", __file__])
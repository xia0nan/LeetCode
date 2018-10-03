# 1. Two Sum
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        matrix = [[ item1 + item2 for item2 in nums] for item1 in nums]
        result = [[i, v.index(target)] for i, v in enumerate(matrix) if target in v][0]
        return result
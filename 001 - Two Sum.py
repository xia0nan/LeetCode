# 1. Two Sum
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_to_index:
                return [i, num_to_index[complement]]
            num_to_index[nums[i]] = i
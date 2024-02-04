# 1. Two Sum
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum2 = nums[i] + nums[j]
                if sum2 == target:
                    return [i,j]
        return False
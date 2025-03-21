from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays using binary search.

        Parameters:
        nums1 (List[int]): First sorted array
        nums2 (List[int]): Second sorted array

        Returns:
        float: The median of the merged sorted arrays
        """

        # Ensure nums1 is the smaller array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Swap to ensure binary search on smaller array

        m, n = len(nums1), len(nums2)  # Sizes of the arrays
        low, high = 0, m  # Binary search range

        while low <= high:
            partitionX = (low + high) // 2  # Partition index for nums1
            partitionY = (m + n + 1) // 2 - partitionX  # Partition index for nums2

            # Edge cases: Handle out-of-bounds indexing
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]

            # Check if partitioning is correct
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total length is odd, median is the max of left partition
                if (m + n) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                # If even, median is average of max left and min right
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2

            # Adjust binary search range
            elif maxLeftX > minRightY:
                high = partitionX - 1  # Move left
            else:
                low = partitionX + 1  # Move right
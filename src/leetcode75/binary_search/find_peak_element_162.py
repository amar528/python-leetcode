import sys
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # element size
        n = len(nums)

        # left and right indices
        left = 0
        right = n - 1

        # loop until left and right cross
        while left <= right:

            # the mid point
            mid = (left + right) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                # go to left side
                right = mid - 1
            elif mid < n - 1 and nums[mid] < nums[mid + 1]:
                # go to right
                left = mid + 1
            else:
                # we have found the result
                return mid

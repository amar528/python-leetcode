from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        places = k % n # rotation - remainder

        # swap
        if places != 0:
            nums[:places], nums[places:] = nums[-places:], nums[:-places]

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        for i in range(n):
            # Given 2 choices, find the maximal value

            # 1st choice is the previous accumulated value
            prev = dp[i - 1]

            # 2nd choice is the current value and the previous non-adjacent house
            curr = nums[i] + dp[i - 2]
            dp[i] = max(prev, curr)

        # maximal result will bubble up to the final element
        return dp[-1]

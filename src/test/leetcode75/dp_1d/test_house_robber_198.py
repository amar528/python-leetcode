from unittest import TestCase

from leetcode75.dp_1d.house_robber_198 import Solution


class TestSolution(TestCase):
    def test_rob_example1(self):
        nums = [1, 2, 3, 1]

        sol = Solution()
        result = sol.rob(nums)

        self.assertEqual(4, result)

    def test_rob_example2(self):
        nums = [2, 7, 9, 3, 1]

        sol = Solution()
        result = sol.rob(nums)

        self.assertEqual(12, result)

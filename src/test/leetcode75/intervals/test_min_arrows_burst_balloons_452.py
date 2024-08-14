from unittest import TestCase

from leetcode75.intervals.min_arrows_burst_balloons_452 import Solution


class TestSolution(TestCase):
    def test_find_min_arrow_shots_example1(self):
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        sol = Solution()

        result = sol.findMinArrowShots(points)

        self.assertEqual(2, result)

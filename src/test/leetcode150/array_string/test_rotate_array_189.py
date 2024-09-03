from unittest import TestCase

from leetcode150.array_string.rotate_array_189 import Solution


class TestSolution(TestCase):
    def test_rotate_example1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3

        sol = Solution()
        sol.rotate(nums, k)

        self.assertListEqual([5, 6, 7, 1, 2, 3, 4], nums)

    def test_rotate_example2(self):
        nums = [1, 2]
        k = 3

        sol = Solution()
        sol.rotate(nums, k)

        self.assertListEqual([2, 1], nums)

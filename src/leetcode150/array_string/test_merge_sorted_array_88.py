from unittest import TestCase

from leetcode150.array_string.merge_sorted_array_88 import Solution


class TestSolution(TestCase):
    def test_merge_example1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3

        sol = Solution()
        sol.merge(nums1, m, nums2, n)

        self.assertListEqual([1, 2, 2, 3, 5, 6], nums1)

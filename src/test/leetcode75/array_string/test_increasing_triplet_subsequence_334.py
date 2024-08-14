from unittest import TestCase

from leetcode75.array_string.increasing_triplet_subsequence_334 import Solution


class TestSolution(TestCase):
    def test_increasing_triplet_example1(self):
        nums = [1, 2, 3, 4, 5]

        sol = Solution()
        result = sol.increasingTriplet(nums)

        self.assertTrue(result)

    def test_increasing_triplet_example2(self):
        nums = [5, 4, 3, 2, 1]

        sol = Solution()
        result = sol.increasingTriplet(nums)

        self.assertFalse(result)

    def test_increasing_triplet_example3(self):
        nums = [2, 1, 5, 0, 4, 6]

        sol = Solution()
        result = sol.increasingTriplet(nums)

        self.assertTrue(result)

    def test_increasing_triplet_example69(self):
        nums = [2, 4, -2, -3]

        sol = Solution()
        result = sol.increasingTriplet(nums)

        self.assertFalse(result)

    def test_increasing_triplet_example74(self):
        nums = [1, 2, 1, 3]

        sol = Solution()
        result = sol.increasingTriplet(nums)

        self.assertTrue(result)

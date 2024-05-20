from unittest import TestCase

from leetcode75.linked_list.listnode import build_list
from leetcode75.linked_list.maximum_twin_sum_linked_list_2130 import Solution


class TestSolution(TestCase):
    def test_pair_sum_example1(self):
        head = build_list([5, 4, 2, 1])

        sol = Solution()
        result = sol.pairSum(head)

        self.assertEqual(6, result)

    def test_pair_sum_example2(self):
        head = build_list([4, 2, 2, 3])

        sol = Solution()
        result = sol.pairSum(head)

        self.assertEqual(7, result)

    def test_pair_sum_example3(self):
        head = build_list([1, 100000])

        sol = Solution()
        result = sol.pairSum(head)

        self.assertEqual(100001, result)

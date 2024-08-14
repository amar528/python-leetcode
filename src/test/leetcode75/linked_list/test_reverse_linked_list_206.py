from unittest import TestCase

import leetcode75.linked_list.listnode as ln
from leetcode75.linked_list.reverse_linked_list_206 import Solution


class TestSolution(TestCase):
    def test_reverse_list_example1(self):
        head = ln.build_list([1, 2, 3, 4, 5])

        sol = Solution()
        result = sol.reverseList(head)

        self.assertListEqual(ln.build_arr(result), [5, 4, 3, 2, 1])

    def test_reverse_list_example2(self):
        head = ln.build_list([1, 2])

        sol = Solution()
        result = sol.reverseList(head)

        self.assertListEqual(ln.build_arr(result), [2, 1])

    def test_reverse_list_example3(self):
        head = ln.build_list(None)

        sol = Solution()
        result = sol.reverseList(head)

        self.assertListEqual(ln.build_arr(result), [])

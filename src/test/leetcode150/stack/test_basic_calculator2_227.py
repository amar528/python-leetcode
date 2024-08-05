from unittest import TestCase

from leetcode150.stack.basic_calculator2_227 import Solution


class TestSolution(TestCase):
    def test_calculate_example1(self):
        self.assertEqual(7, Solution().calculate("3+2*2"))

    def test_calculate_example2(self):
        self.assertEqual(13, Solution().calculate("14-3/2"))

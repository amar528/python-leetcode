from unittest import TestCase

from leetcode150.stack.basic_calculator_224 import Solution


class TestSolution(TestCase):
    def test_calculate_example1(self):
        self.assertEqual(2, Solution().calculate("1 + 1"))

    def test_calculate_example2(self):
        self.assertEqual(3, Solution().calculate(" 2-1 + 2 "))

    def test_calculate_example3(self):
        self.assertEqual(23, Solution().calculate("(1+(4+5+2)-3)+(6+8)"))

    def test_calculate_example4(self):
        self.assertEqual(3, Solution().calculate("1-(     -2)"))

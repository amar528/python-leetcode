from unittest import TestCase

from leetcode150.stack.valid_parenthesis_20 import Solution


class TestSolution(TestCase):
    def test_is_valid_example1(self):
        self.assertTrue(Solution().isValid("()"))

    def test_is_valid_example2(self):
        self.assertTrue(Solution().isValid("()[]{}"))

    def test_is_valid_example3(self):
        self.assertFalse(Solution().isValid("(]"))

    def test_is_valid_example4(self):
        self.assertFalse(Solution().isValid("))"))

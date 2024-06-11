from unittest import TestCase

from leetcode75.graphs.dfs.evaluate_division_399 import Solution


class TestSolution(TestCase):

    def test_calc_equation_example1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

        sol = Solution()
        result = sol.calcEquation(equations, values, queries)

        self.assertListEqual([6.00000, 0.50000, -1.00000, 1.00000, -1.00000], result)

    def test_calc_equation_example2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

        sol = Solution()
        result = sol.calcEquation(equations, values, queries)

        self.assertListEqual([3.75000, 0.40000, 5.00000, 0.20000], result)

    def test_calc_equation_example3(self):
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]

        sol = Solution()
        result = sol.calcEquation(equations, values, queries)

        self.assertListEqual([0.50000, 2.00000, -1.00000, -1.00000], result)

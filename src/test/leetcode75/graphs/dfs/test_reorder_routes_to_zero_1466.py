from unittest import TestCase

from leetcode75.graphs.dfs.reorder_routes_to_zero_1466 import Solution


class TestSolution(TestCase):
    def test_min_reorder_example1(self):
        n = 6
        connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

        sol = Solution()
        result = sol.minReorder(n, connections)

        self.assertEqual(3, result)

    def test_min_reorder_example2(self):
        n = 5
        connections = [[1, 0], [1, 2], [3, 2], [3, 4]]

        sol = Solution()
        result = sol.minReorder(n, connections)

        self.assertEqual(2, result)

    def test_min_reorder_example3(self):
        n = 3
        connections = [[1, 0], [2, 0]]

        sol = Solution()
        result = sol.minReorder(n, connections)

        self.assertEqual(0, result)

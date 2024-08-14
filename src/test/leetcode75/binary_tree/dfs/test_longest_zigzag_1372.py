from unittest import TestCase

from leetcode75.binary_tree.dfs.longest_zigzag_1372 import Solution
from leetcode75.binary_tree.treenode import TreeNode


class TestSolution(TestCase):
    def test_longest_zig_zag_example1(self):
        root = TreeNode(1,
                        None,
                        TreeNode(1,
                                 TreeNode(1),
                                 TreeNode(1,
                                          TreeNode(1,
                                                   None,
                                                   TreeNode(1,
                                                            None,
                                                            TreeNode(1))),
                                          TreeNode(1))))
        sol = Solution()
        result = sol.longestZigZag(root)

        self.assertEqual(3, result)

    def test_longest_zig_zag_example2(self):
        root = TreeNode(1)
        sol = Solution()
        result = sol.longestZigZag(root)

        self.assertEqual(0, result)

    def test_longest_zig_zag_example26(self):
        root = TreeNode(1,
                        TreeNode(2, TreeNode(4), None),
                        TreeNode(3, None, TreeNode(5))
                        )
        sol = Solution()
        result = sol.longestZigZag(root)

        self.assertEqual(1, result)

from unittest import TestCase

from leetcode75.binary_tree.treenode import *
from leetcode75.bst.delete_node_in_bst_450 import Solution


class TestSolution(TestCase):
    def test_delete_node_example1(self):
        root = TreeNode(5,
                        TreeNode(3,
                                 TreeNode(2),
                                 TreeNode(4)),
                        TreeNode(6,
                                 None,
                                 TreeNode(7))
                        )

        key = 3
        sol = Solution()

        result = sol.deleteNode(root, key)
        self.assertIsNotNone(result)

        self.assertEqual(5, result.val)
        self.assertEqual(2, result.left.val)
        self.assertEqual(6, result.right.val)

        self.assertIsNone(result.left.left)
        self.assertEqual(4, result.left.right.val)

    def test_delete_node_example2(self):
        root = TreeNode(0)

        key = 0
        sol = Solution()

        sol.deleteNode(root, key)

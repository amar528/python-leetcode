from unittest import TestCase

from leetcode75.binary_tree.treenode import *
from leetcode75.bst.delete_node_in_bst_450 import Solution


class TestSolution(TestCase):


    def test_delete_node_example2(self):
        root = TreeNode(0)

        key = 0
        sol = Solution()

        sol.deleteNode(root, key)

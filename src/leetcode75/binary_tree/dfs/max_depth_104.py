from typing import Optional

from leetcode75.binary_tree.treenode import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # base case: null node
        if not root:
            return 0

        # return this level (1) plus the maximum of the left and right subtrees
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

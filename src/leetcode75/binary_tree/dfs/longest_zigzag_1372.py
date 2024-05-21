from typing import Optional

from leetcode75.binary_tree.treenode import TreeNode


class Solution:
    def __init__(self):
        self.result = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node, left_depth, right_depth):
            # update the maximum zigzag depth so far
            self.result = max(self.result, left_depth, right_depth)

            # if we have a valid left child node, continue recursion with the right depth
            if node.left:
                dfs(node.left, right_depth + 1, 0)

            # if we have a valid right child node, continue recursion with the left depth
            if node.right:
                dfs(node.right, 0, left_depth + 1)

        dfs(root, 0, 0)
        return self.result

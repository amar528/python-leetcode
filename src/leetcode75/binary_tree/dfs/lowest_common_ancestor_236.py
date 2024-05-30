from leetcode75.binary_tree.treenode import TreeNode


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):

            # base case, end recursive subtree
            if not node:
                return None

            # Either node can be the LCA of itself, also we want to end the
            # recursion when we hit p or q
            if node == p or node == q:
                return node

            # Otherwise, we recurse for left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # If we have found both p and q, then our current node must be the closest ancestor
            if left and right:
                return node

            # Otherwise, we return any non-null result from the left or right subtrees
            return left or right

        return dfs(root)

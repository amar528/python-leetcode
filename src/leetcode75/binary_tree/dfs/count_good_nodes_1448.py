from leetcode75.binary_tree.treenode import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        def dfs(current, current_max):

            if not current:
                return 0

            count = 0

            if current_max <= current.val:
                # this is a 'good node' as it has a value greater or equal to the current maximum
                count = 1

            current_max = max(current_max, current.val)

            # recurse left and right, adding to our current count
            return count + dfs(current.left, current_max) + dfs(current.right, current_max)

        # start dfs from the root, current maximum is the root value
        return dfs(root, root.val)

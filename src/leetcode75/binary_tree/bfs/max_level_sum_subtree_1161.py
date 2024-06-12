import collections
from typing import Optional

from leetcode75.binary_tree.treenode import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        # queue items are (level, node)
        # enqueue the root
        queue = collections.deque([(1, root)])

        # keep track of sums per level : level: sum
        level_sums = collections.defaultdict(int)

        while queue:

            # deque the current level and node
            level, node = queue.popleft()

            # add the node value to the total for this level (key)
            level_sums[level] += node.val

            if node.left:
                # enqueue left child for next level
                queue.append((level + 1, node.left))

            if node.right:
                # enqueue right child for the next level
                queue.append((level + 1, node.right))

        # return the maximum sum of all levels
        return max(level_sums, key=level_sums.get)

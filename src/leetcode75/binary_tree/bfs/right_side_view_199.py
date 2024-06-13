import collections
from typing import Optional, List

from leetcode75.binary_tree.treenode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []
        q = collections.deque([root])

        while q:

            # pointer to the right most node, that is the node that is seen for this level
            # as if looking from the right of the tree
            right_most = None

            # process all nodes at this level
            # here we use range on the current length of the queue at the start of iteration
            # this will not be affected by appending the child nodes
            for _ in range(len(q)):

                current = q.popleft()

                if current:
                    # we work left to right, so update the right most
                    right_most = current

                    # enqueue the child nodes for the next level
                    q.append(current.left)
                    q.append(current.right)

            # this level has completed, so add right most result if it's valid
            if right_most:
                result.append(right_most.val)

        return result

from typing import Optional

from leetcode75.binary_tree.treenode import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def find(node, parent):
            if not node:
                return node, parent

            if node.val == key:
                return node, parent

            if key < node.val:
                return find(node.left, node)
            else:
                return find(node.right, node)

        def delete(node, parent):
            if node.left and node.right and node.left.val < node.right.val:
                parent.left = node.left
                parent.left.left = node.right
            else:
                parent.left = node.right

        # step 1 - find the node and its parent
        found_node, found_parent = find(root, None)

        if not found_node:
            return root

        # step 2 - delete the node and return the root
        delete(found_node, found_parent)
        return root

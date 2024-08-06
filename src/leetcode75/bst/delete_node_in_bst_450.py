from typing import Optional

from leetcode75.binary_tree.treenode import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root and key == root.val:
            return None

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

            # handle case when node to be deleted is the root node
            if node == parent:
                pass

            if node.left and node.right and node.left.val < node.right.val:
                parent.left = node.left
                if parent.left:
                    parent.left.right = node.right
            else:
                parent.left = node.right

        # step 1 - find the node and its parent
        found_node, found_parent = find(root, root)

        # node to be deleted does not exist
        if not found_node:
            return root

        # step 2 - delete the node and return the (potential) new root
        new_root = delete(found_node, found_parent)
        return new_root

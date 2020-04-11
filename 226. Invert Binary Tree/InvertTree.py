"""
Invert a binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        T(n) = O(n) -- traversed all nodes
        S(n) = O(n) -- recursion stack for totally unbalanced tree
        """
        if root is None:
            return root
        if not (root.left is None and root.right is None):
            flipped_left = self.invertTree(root.right)
            flipped_right = self.invertTree(root.left)
            root.left = flipped_left
            root.right = flipped_right
        return root

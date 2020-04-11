"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        T(n) = O(n) -- traversed each node in the BST
        S(n) = O(n) -- keepping recursion stack for totally unbalanced tree
        """
        def recur(node: TreeNode, lo: float, hi: float):
            if not node:
                return True
            if node.val <= lo or node.val >= hi:
                return False
            return recur(
                node.left,
                lo,
                node.val) and recur(
                node.right,
                node.val,
                hi)

        lo = float('-inf')
        hi = float('inf')
        return recur(root, lo, hi)

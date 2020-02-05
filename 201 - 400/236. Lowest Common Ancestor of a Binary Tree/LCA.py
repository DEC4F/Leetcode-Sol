"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.ans = None
    
    def lowestCommonAncestor_recur(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        T(n) = O(n) -- traverse all nodes in worst case
        S(n) = O(n) -- keepping recur stack for totally unbalanced binary tree
        """
        def recur(curr_node: 'TreeNode') -> bool:
            if not curr_node:
                return False

            # left branch is true if p or q in left branch
            left = recur(curr_node.left)
            # right branch is true if p or q in right branch
            right = recur(curr_node.right)
            # mid is true if current at p or q
            mid = curr_node == p or curr_node == q

            # more than 1 var are true at LCA
            if mid+left+right >= 2:
                self.ans = curr_node

            return mid or left or right
        recur(root)
        return self.ans
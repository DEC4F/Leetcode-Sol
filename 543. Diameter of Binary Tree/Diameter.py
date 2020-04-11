"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        if not root:
            return 0
        self.res = 0
        def dfs(node) -> int:
            if not node:
                return 0
            L = dfs(node.left)
            R = dfs(node.right)
            self.res = max(self.res, L + R + 1)
            cur = 1 + max(L, R)
            return cur
        dfs(root)
        return self.res - 1

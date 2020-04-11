"""
Given a binary tree root, a ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right then move to the right child of the current node otherwise move to the left child.
Change the direction from right to left or right to left.
Repeat the second and third step until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        self.res = 0
        def dfs(node, acc, is_left) -> int:
            if not node:
                return
            self.res = max(self.res, acc)
            if is_left:
                dfs(node.right, acc + 1, False)
                dfs(node.left, 1, True)
            else:
                dfs(node.right, 1, False)
                dfs(node.left, acc + 1, True)
        dfs(root.left, 1, True)
        dfs(root.right, 1, False)
        return self.res

    def longestZigZag_lee215(self, root: TreeNode) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        def dfs(node) -> int:
            if not node:
                return [-1, -1, -1]
            L = dfs(node.left)
            R = dfs(node.right)
            return [L[1] + 1, R[0] + 1, max(L[1] + 1, R[0] + 1, L[2], R[2])]
        return dfs(root)[2]
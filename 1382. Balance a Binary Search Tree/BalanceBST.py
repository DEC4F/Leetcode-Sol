"""
Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        flatten = []

        def dfs(node: TreeNode) -> None:
            if node:
                dfs(node.left)
                flatten.append(node.val)
                dfs(node.right)

        def balance(lo, hi) -> TreeNode:
            if lo <= hi:
                mid = (lo + hi) // 2
                node = TreeNode(flatten[mid])
                node.left = balance(lo, mid - 1)
                node.right = balance(mid + 1, hi)
                return node

        dfs(root)
        return balance(0, len(flatten) - 1)
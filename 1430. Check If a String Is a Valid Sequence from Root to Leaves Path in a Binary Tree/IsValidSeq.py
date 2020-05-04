"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree.

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        def dfs(node, i):
            if node.left is None and node.right is None and i == len(arr) - 1:
                return node.val == arr[i]
            if i == len(arr) - 1:
                return False
            L = dfs(node.left, i + 1) if node.left is not None else False
            R = dfs(node.right, i + 1) if node.right is not None else False
            return (node.val == arr[i]) and (L or R)
        return dfs(root, 0)
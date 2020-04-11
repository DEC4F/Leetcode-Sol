"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    max_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        """
        T(n) = O(n) -- traversed all nodes
        S(n) = O(n) -- at most n nodes in recursion stack when the tree is totally unbalanced
        """
        self.maxGain(root)
        return self.max_sum

    def maxGain(self, node: TreeNode) -> int:
        if node is None:
            return 0
        left_gain = max(0, self.maxGain(node.left))
        right_gain = max(0, self.maxGain(node.right))

        self.max_sum = max(self.max_sum, node.val + left_gain + right_gain)
        return node.val + max(left_gain, right_gain)

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth_recur(self, root: TreeNode) -> int:
        """
        T(n) = O(n) -- traversed all nodes
        S(n) = O(n) -- recursion stack
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def maxDepth_iter(self, root: TreeNode) -> int:
        """
        T(n) = O(n) -- traversed all nodes
        S(n) = O(n) -- keep a stack
        """
        if not root:
            return 0

        stack = [(1, root)]
        max_depth = 0
        while stack:
            lv, node = stack.pop()
            if node:
                max_depth = max(max_depth, lv)
                stack.append((lv + 1, node.left))
                stack.append((lv + 1, node.right))
        return max_depth

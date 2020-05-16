"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        def dfs(node, p_max):
            if not node:
                return
            if node.val >= p_max:
                p_max = node.val
                self.res += 1
            dfs(node.left, p_max)
            dfs(node.right, p_max)
        self.res = 0
        dfs(root, root.val)
        return self.res

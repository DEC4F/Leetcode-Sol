# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        """
        T(n) = O(n) -- visit all nodes in worst case
        S(n) = O(n) -- size of recursion stack in totally unbalanced tree
        """
        def dfs(node: TreeNode) -> bool:
            nonlocal root
            if node is None:
                return True
            if node.val != root.val:
                return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)

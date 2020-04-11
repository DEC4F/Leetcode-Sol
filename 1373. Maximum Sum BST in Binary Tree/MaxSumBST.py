"""
Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

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
    def maxSumBST(self, root: TreeNode) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        def dfs(node: TreeNode):
            """
            returns [min_sofar, max_sofar, sum_at_this_node, is_BST]
            """
            if not node:
                return float('inf'), float('-inf'), 0, True
            L = dfs(node.left)
            R = dfs(node.right)
            cur_min = min(L[0], node.val)
            cur_max = max(R[1], node.val)
            cur_sum = -1
            is_BST = False
            if L[1] < node.val < R[0] and L[3] and R[3]:
                is_BST = True
                cur_sum = L[2] + R[2] + node.val
            self.res = max(self.res, cur_sum)
            return cur_min, cur_max, cur_sum, is_BST
        self.res = 0
        dfs(root)
        return self.res
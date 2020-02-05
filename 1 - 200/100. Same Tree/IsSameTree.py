"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree_recur(self, p: TreeNode, q: TreeNode) -> bool:
        """
        T(n) = O(n) -- validate every node
        S(n) = O(n) -- keepping recur stack for totally unbalanced tree
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree_recur(p.left, q.left) and self.isSameTree_recur(p.right, q.right)

    def isSameTree_iter(self, p: TreeNode, q: TreeNode) -> bool:
        """
        T(n) = O(n) -- validate every node
        S(n) = O(n) -- keepping queue for totally unbalanced tree
        """
        from collections import deque
        if not self.check(p, q):
            return False
        
        dq = deque([(p, q)])
        while dq:
            p, q = dq.popleft()
            if not self.check(p, q):
                return False
            if p:
                dq.append((p.left, q.left))
                dq.append((p.right, q.right))
        return True
    
    def check(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return True
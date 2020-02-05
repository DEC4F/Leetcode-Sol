"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree_bfs_recursive_compare(self, s: TreeNode, t: TreeNode) -> bool:
        """
        T(n) = O(m*n) -- visit all nodes and compared almost all nodes in t in worst case
        S(n) = O(m+n) -- size of dq plus recursion stack in worst case
        """
        if not s and not t:
            return True
        if not s or not t:
            return False

        from collections import deque
        dq = deque([s])
        while dq:
            node = dq.popleft()
            if node is not None:
                if self.compare(node, t):
                    return True
                dq.append(node.left)
                dq.append(node.right)
        return False

    def compare(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if (s is None or t is None):
            return False
        return s.val == t.val and self.compare(s.left, t.left) and self.compare(s.right, t.right)

    def isSubtree_string_search(self, s: TreeNode, t: TreeNode) -> bool:
        """
        T(n) = O(m^2 + n^2) -- string concat time for s and t
        S(n) = O(m + n) -- size of two strings
        """
        if not s and not t:
            return True
        if not s or not t:
            return False

        s1 = self.serialize(s, True)
        t1 = self.serialize(t, True)
        return t1 in s1

    def serialize(self, node: TreeNode, left: bool) -> str:
        if node is None:
            if left:
                return 'lnull '
            else:
                return 'rnull '
        return '#' + str(node.val) + ' ' + self.serialize(node.left, True) + self.serialize(node.right, False)

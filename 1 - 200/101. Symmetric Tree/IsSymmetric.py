"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric_iter(self, root: TreeNode) -> bool:
        """
        T(n) = O(n) -- visited all nodes
        S(n) = O(n) -- store in a queue
        """
        if not root:
            return True
        dq = deque([root,root])
        while dq:
            node1 = dq.popleft()
            node2 = dq.popleft()
            # both null, move to next pair
            if not node1 and not node2:
                continue
            # value mismatch
            elif (not node1 or not node2) or node1.val != node2.val:
                return False
            # value match, append children and move to next pair
            else:
                dq.append(node1.left)
                dq.append(node2.right)
                dq.append(node1.right)
                dq.append(node2.left)
        return True

    def isSymmetric_recur(self, root: TreeNode) -> bool:
        """
        T(n) = O(n) -- visited all nodes
        S(n) = O(n) -- recursion stack
        """
        if not root:
            return True
        def isMirror(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            else:
                return node1.val == node2.val and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
        return isMirror(root, root)

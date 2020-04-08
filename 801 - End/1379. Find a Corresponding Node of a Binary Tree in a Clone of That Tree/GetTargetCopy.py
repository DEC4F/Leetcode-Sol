"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy_BFS(self, original: TreeNode,
                                cloned: TreeNode,
                                target: TreeNode) -> TreeNode:
        """
        T(n) = O(n)
        S(n) = O(n) = 2n
        """
        q1 = deque([original])
        q2 = deque([cloned])
        while q1:
            node = q1.popleft()
            c_node = q2.popleft()
            if node is None:
                continue
            if node == target:
                return c_node
            q1.append(node.left)
            q1.append(node.right)
            q2.append(c_node.left)
            q2.append(c_node.right)

    def getTargetCopy_DFS(self, original: TreeNode,
                                cloned: TreeNode,
                                target: TreeNode) -> TreeNode:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        def dfs(node: TreeNode, c_node: TreeNode) -> TreeNode:
            if node is None:
                return None
            if node == target:
                return c_node
            return dfs(node.left, c_node.left) or dfs(node.right, c_node.right)
        return dfs(original, cloned)
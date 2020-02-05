# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def findBottomLeftValue_bfs(self, root: TreeNode) -> int:
        """
        T(n) = O(n) -- traversed all nodes
        S(n) = O(n) -- used dq to hold all nodes
        """
        dq = deque([[root]])
        ans = root.val
        while dq:
            next_lv = []
            curr_lv = dq.popleft()
            for node in curr_lv:
                if node.left is not None:
                    next_lv.append(node.left)
                if node.right is not None:
                    next_lv.append(node.right)
            dq.append(next_lv)
            if len(next_lv) > 0:
                ans = next_lv[0].val
            else:
                return ans

    def findBottomLeftValue_dfs(self, root: TreeNode) -> int:
        """
        T(n) = O(n) -- traversed all nodes
        S(n) = O(n) -- size of recursion stack in totally unbalanced case
        """
        ans = root.val
        max_lv = 1

        def dfs(node: TreeNode, lv: int) -> None:
            nonlocal max_lv
            nonlocal ans

            if node is None:
                return
            if lv > max_lv:
                ans = node.val
                max_lv = lv
            dfs(node.left, lv+1)
            dfs(node.right, lv+1)

        dfs(root, max_lv)
        return ans

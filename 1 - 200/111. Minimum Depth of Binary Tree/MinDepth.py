# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        T(n) = O(n) -- will visit all nodes in worst case (totally unbalanced)
        S(n) = O(n) -- will store all nodes in worst case (totally unbalanced)
        """
        from collections import deque
        if not root:
            return 0
        dq = deque([[root]])
        lv = 1
        while dq:
            cur_lv = dq.popleft()
            new_lv = []
            for node in cur_lv:
                if node.left is None and node.right is None:
                    return lv
                if node.left is not None:
                    new_lv.append(node.left)
                if node.right is not None:
                    new_lv.append(node.right)
            dq.append(new_lv)
            lv += 1

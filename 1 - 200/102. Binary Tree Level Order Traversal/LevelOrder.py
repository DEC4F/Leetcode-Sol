# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        T(n) = O(n) -- traverse n nodes
        S(n) = O(n) -- keepping the queue
        """
        from collections import deque
        ans = []
        # if root is null, return an empty list
        if not root:
            return ans

        dq = deque([root,])
        lv = 0
        while dq:
            ans.append([])
            for _ in range(len(dq)):
                node = dq.popleft()
                if node:
                    ans[lv].append(node.val)
                # append its left and right children
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            lv += 1
        return ans
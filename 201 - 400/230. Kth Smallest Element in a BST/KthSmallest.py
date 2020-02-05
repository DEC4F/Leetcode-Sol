# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest_inorder_recur(self, root: TreeNode, k: int) -> int:
        """
        T(n) = O(n) -- visited all nodes
        S(n) = O(n) -- size of recursion stack in worst case
        """
        arr = []
        def dfs(node: TreeNode) -> None:
            if node is None:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        return arr[k-1]

    def kthSmallest_inorder_iter(self, root: TreeNode, k: int) -> int:
        """
        H is tree height
        T(n) = O(H + k) -- only visit all the way to the bottom and backup to k nodes
        S(n) = O(H + k) -- stored upto H + k nodes in stack
        """
        if root is None:
            return root
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        T(n) = T(n/k) + T(n/(n-k)) + n = O(n^2) -- worst case if nums is reversely sorted
        S(n) = O(n) -- size of recursion stack in worst case
        """
        def construct(nums: List[int]) -> TreeNode:
            # find max node val of cur subarray
            idx = 0
            for i, n in enumerate(nums):
                if nums[idx] < n:
                    idx = i
            node = TreeNode(nums[idx])
            if len(nums[:idx]) > 0:
                node.left = construct(nums[:idx])
            if len(nums[idx + 1:]) > 0:
                node.right = construct(nums[idx + 1:])
            return node
        return construct(nums)

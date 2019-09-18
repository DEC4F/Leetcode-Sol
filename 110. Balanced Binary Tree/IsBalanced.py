"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.balanced = True
    
    def isBalanced(self, root: TreeNode) -> bool:
        """
        T(n) = O()
        S(n) = O(n) -- recursion stack of totally unbalanced tree
        """
        if not root:
            return True
        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            left_depth = depth(node.left)
            right_height = depth(node.right)
            if abs(left_depth-right_height) > 1:
                self.balanced = False
                return -1
            return max(left_depth, right_height)+1
        depth(root)
        return self.balanced
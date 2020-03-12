"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        """
        T(n) = O(n) -- visit all nodes
        S(n) = O(n) -- size of stack and output array
        """
        if not root:
            return []
        if len(to_delete) < 1:
            return [root]

        def dfs(node: TreeNode, is_root: bool, forest: List[TreeNode]) -> (List[TreeNode], TreeNode):
            # end of current branch due to exhaustion
            if not node:
                return forest, None
            is_del = node.val in to_delete
            # add new node if parents is del and current node is not to be del
            if is_root and not is_del:
                forest.append(node)
            forest, node.left = dfs(node.left, is_del, forest)
            forest, node.right = dfs(node.right, is_del, forest)
            if is_del:
                return forest, None
            return forest, node

        res, _ = dfs(root, True, [])
        return res
"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        
        T(n) = O(n) -- traversed every node
        S(n) = O(n) -- queue stored every node
        """
        ans = []
        if root is None:
            return ans
        dq = deque([root,])
        while dq:
            node = dq.popleft()
            if node is None:
                ans.append(None)
            else:
                ans.append(node.val)
                dq.append(node.left)
                dq.append(node.right)
        return ans
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        
        T(n) = O(n) -- traversed every node
        S(n) = O(n) -- queue stored every node
        """
        if data is None or len(data) == 0:
            return data
        root = TreeNode(data[0])
        dq = deque([root,])
        lv = 1
        while dq and lv < len(data):
            node = dq.popleft()
            if data[lv] is not None:
                node.left = TreeNode(data[lv])
                dq.append(node.left)
            lv += 1
            if data[lv] is not None:
                node.right = TreeNode(data[lv])
                dq.append(node.right)
            lv += 1
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
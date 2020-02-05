"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Codec:

    def serialize(self, root):
        """
        T(n) = O(n) -- visited all children
        S(n) = O(n) -- size of recursion stack in worst case
        """
        s_dict = {}
        if not root:
            return s_dict
        s_dict['value'] = root.val
        s_dict['children'] = [self.serialize(child) for child in root.children]
        return s_dict

    def deserialize(self, data):
        """
        T(n) = O(n) -- visited all children
        S(n) = O(n) -- size of recursion stack in worst case
        """
        if not data:
            return None
        root = Node(data['value'], [self.deserialize(child) for child in data['children']])
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
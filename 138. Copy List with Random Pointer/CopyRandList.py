"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:

    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        T(n) = O(n) -- explore n nodes
        S(n) = O(n) -- size of stack
        """
        if head is None:
            return None
        if head in self.visited:
            return self.visited[head]

        node = Node(head.val)
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node

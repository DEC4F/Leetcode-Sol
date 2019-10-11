# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        T(n) = O(n) -- fast and slow ptr
        S(n) = O(1)
        """
        if not (head or head.next):
            return head
        turtle = hare = head
        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next
        return turtle
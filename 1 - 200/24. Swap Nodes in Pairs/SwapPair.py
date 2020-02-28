# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next
        return dummy.next
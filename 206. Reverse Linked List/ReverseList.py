"""
Reverse a singly linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList_recur(self, head: ListNode) -> ListNode:
        pass
        
    def reverseList_iter(self, head: ListNode) -> ListNode:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        prev = None
        while head:
            ptr = head
            head = head.next
            ptr.next = prev
            prev = ptr
        return prev
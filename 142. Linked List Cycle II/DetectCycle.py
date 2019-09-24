"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def detectCycle_seen(self, head: ListNode) -> ListNode:
        """
        T(n) = O(n) -- traversed linearly
        S(n) = O(n) -- used a list
        """
        if not head:
            return None
        ptr = head
        seen = []
        while ptr:
            if ptr in seen:
                return ptr
            else:
                seen.append(ptr)
            ptr = ptr.next
        return None;

    def detectCycle_fast_slow_ptr(self, head: ListNode) -> ListNode:
        """
        T(n) = O(n) -- (F+C-h) + F <= 2n
        S(n) = O(1) -- const space
        """
        if not head:
            return None
        tor = hare = head
        first_run = True
        while tor or hare:
            if tor == hare and not first_run:
                hare = head
                while hare != tor:
                    hare = hare.next
                    tor = tor.next
                return tor
            else:
                if not tor.next or not hare.next or not hare.next.next:
                    return None
                first_run = False
                tor = tor.next
                hare = hare.next.next
        return None
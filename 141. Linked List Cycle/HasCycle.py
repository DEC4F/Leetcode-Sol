"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle_fast_slow_ptr(self, head: ListNode) -> bool:
        """
        T(n) = O(n) -- F+C-h < n
        S(n) = O(1) -- const space
        """
        if not head:
            return False
        fast = slow = head
        first_run = True
        while fast and slow:
            if fast == slow and not first_run:
                return True
            else:
                if not fast.next or not slow.next or not fast.next.next:
                    return None
            first_run = False
            fast = fast.next.next
            slow = slow.next
        return False
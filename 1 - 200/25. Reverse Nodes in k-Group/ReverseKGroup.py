# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        if not head or k <= 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        nxt = dummy.next
        stack = []
        while nxt:
            while len(stack) < k and nxt:
                stack.append(nxt)
                nxt = nxt.next
            if len(stack) < k:
                return dummy.next
            while len(stack) > 0:
                cur.next = stack.pop()
                cur = cur.next
            cur.next = nxt
        return dummy.next
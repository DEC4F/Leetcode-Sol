"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        carry = 0
        curr = ListNode(0)
        head = curr
        while l1 or l2 or carry:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, r = divmod(val1 + val2 + carry, 10)
            curr.next = ListNode(r)
            curr = curr.next
        # skipping trailing 0 in the head
        return head.next


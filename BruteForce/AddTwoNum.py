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
        num_l1 = self.list_to_num(self.reverse_linked_list(l1))
        num_l2 = self.list_to_num(self.reverse_linked_list(l2))
        num_l3 = num_l1 + num_l2
        return self.reverse_linked_list(self.num_to_list(num_l3))

    def list_to_num(self, l: ListNode) -> int:
        curr = l
        n = []
        while curr != None:
            n.append(curr.val)
            curr = curr.next
        return int(''.join(list(map(str, n))))

    def num_to_list(self, n: int) -> ListNode:
        n = [int(x) for x in str(n)]
        head = ListNode(n.pop(0))
        curr = head
        while n:
            l = ListNode(n.pop(0))
            curr.next = l
            curr = l
        return head

    def reverse_linked_list(self, head:ListNode) -> ListNode:
        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev


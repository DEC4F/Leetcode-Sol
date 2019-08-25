"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#     overriding comparator for min heap
#     def __lt__(self, node):
#         return self.val < node.val

#    def __gt__(self, node):
#         return self.val > node.val

import heapq as hq

class Solution:

    def mergeKLists_div_and_conquer(self, lists: List[ListNode]) -> ListNode:
        """
        T(n) = O(nlogk) -- merging logk lists in O(n) time
        S(n) = O(1)
        """
        if not any(lists):
            return None
        amount = len(lists)
        interval = 1
        if amount == 0:
            return lists
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1:ListNode, l2:ListNode) -> ListNode:
        head = ptr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next

        if not l1:
            ptr.next = l2
        if not l2:
            ptr.next = l1
        return head.next

    def mergeKLists_min_heap(self, lists: List[ListNode]) -> ListNode:
        """
        T(n) = O(nlogk) -- using pq that finds the min val at O(logk)
        S(n) = O(n)
        """
        head = ptr = ListNode(0)
        while any(lists):
            lists = [e for e in lists if e is not None]
            hq.heapify(lists)
            temp = hq.heappop(lists)
            hq.heappush(lists, temp.next)
            ptr.next = temp
        return head.next

    def mergeKLists_table(self, lists: List[ListNode]) -> ListNode:
        """
        T(n) = O(kn)
        S(n) = O(1)
        """
        head = ptr = ListNode(0)
        while any(lists):
            min_idx = None
            for i, node in enumerate(lists):
                if node is None:
                    continue
                if min_idx is None:
                    min_idx = i
                elif node.val < lists[min_idx].val:
                    min_idx = i
            ptr.next = lists[min_idx]
            ptr = ptr.next
            lists[min_idx] = lists[min_idx].next
        return head.next

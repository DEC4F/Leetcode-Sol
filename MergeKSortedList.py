# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ptr = ListNode(0)
        while not all(node is None for node in lists):
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
            lists[min_idx] = ptr.next
        return head.next

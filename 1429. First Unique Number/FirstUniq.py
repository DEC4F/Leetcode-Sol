"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None


class FirstUnique:

    def __init__(self, nums: List[int]):
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        self.mp = {}
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        for n in nums:
            self.add(n)

    def addToTail(self, node: "Node"):
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def removeNode(self, node: "Node"):
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        if node.next is None or node.prev is None:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None

    def showFirstUnique(self) -> int:
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        node = self.head.next
        return -1 if node == self.tail else node.val

    def add(self, value: int) -> None:
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        if self.mp.get(value) is None:
            node = Node(value)
            self.mp[value] = node
            self.addToTail(node)
        else:
            self.removeNode(self.mp.get(value))


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

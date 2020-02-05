class DLNode():
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCacheDoublyLinkedList:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : DLNode pair
        self.head = DLNode(-1, -1)
        self.tail = DLNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        T(n) = O(n) -- worst case for get key in cache
        S(n) = O(n) -- size of cache dict
        """
        node = self.cache.get(key)
        if not node:
            return -1
        self.move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        T(n) = O(n) -- worst case for get key in cache
        S(n) = O(n) -- size of cache dict
        """
        node = self.cache.get(key)
        if not node:
            if len(self.cache)+1 > self.capacity:
                last = self.pop_tail()
                self.cache.pop(last.key, last)
            node = DLNode(key, value)
            self.cache[key] = node
            self.add(node)
        else:
            node.value = value
            self.move_to_front(node)
        
    def add(self, node: DLNode) -> None:
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
    
    def remove(self, node: DLNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def move_to_front(self, node: DLNode) -> None:
        self.remove(node)
        self.add(node)
    
    def pop_tail(self) -> DLNode:
        last = self.tail.prev
        self.remove(last)
        return last
    
class LRUCacheNSquare:

    """
    Time Limit Exceeded
    """

    def __init__(self, capacity: int):
        self.LRU = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        T(n) = O(n^2)
        S(n) = O(1)
        """
        for i in range(len(self.LRU)):
            if self.LRU[i][0] == key:
                self.bubble_up(i)
                return self.LRU[0][1]
        return -1

    def put(self, key: int, value: int) -> None:
        """
        T(n) = O(n^2)
        S(n) = O(1)
        """
        for i in range(len(self.LRU)):
            if self.LRU[i][0] == key:
                self.bubble_up(i)
                self.LRU[0] = (key, value)
                return
        new_pair = (key, value)
        if len(self.LRU) >= self.capacity:
            self.LRU.pop(self.capacity-1)
        idx = len(self.LRU)
        self.LRU[idx] = new_pair
        self.bubble_up(idx)
    
    def bubble_up(self, i: int) -> None:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        while i != 0:
            self.LRU[i], self.LRU[i-1] = self.LRU[i-1], self.LRU[i]
            i -= 1

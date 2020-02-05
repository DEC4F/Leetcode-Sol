"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
"""

class NumArrayRecursive:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.nums = nums
        from math import ceil, log
        self.stree = [0]*(2**(ceil(log(len(nums), 2))+1))
        def _build_tree(node: int, start: int, end: int) -> None:
            """
            T(n) = O(n) -- traverse and store all nodes including range sum
            S(n) = O(n) -- size of recursion stack in complete unbalanced tree and size of seg tree
            """
            if start == end:
                self.stree[node] = self.nums[start]
                return
            left_node, right_node = 2 * node + 1, 2 * node + 2
            mid = (start + end) // 2
            _build_tree(left_node, start, mid)
            _build_tree(right_node, mid+1, end)
            self.stree[node] = self.stree[left_node] + self.stree[right_node]

        _build_tree(0, 0, len(nums)-1)

    def update(self, i: int, val: int) -> None:
        def update_tree(node: int, start: int, end: int) -> None:
            """
            T(n) = O(logn)
            S(n) = O(1)
            """
            if start == end:
                self.nums[i] = val
                self.stree[node] = val
                return

            left_node, right_node = left_node, right_node = 2 * node + 1, 2 * node + 2
            mid = (start + end) // 2

            if start <= i and i <= mid:
                update_tree(left_node, start, mid)
            else:
                update_tree(right_node, mid + 1, end)
            self.stree[node] = self.stree[left_node] + self.stree[right_node]
        update_tree(0, 0, len(self.nums)-1)

    def sumRange(self, i: int, j: int) -> int:
        def query(node: int, start: int, end: int) -> int:
            """
            T(n) = O(logn)
            S(n) = O(1)
            """
            if j < start or i > end:
                return 0
            if start == end:
                return self.stree[node]

            mid = (start + end) // 2
            left_node, right_node = left_node, right_node = 2 * node + 1, 2 * node + 2

            L_sum = query(left_node, start, mid)
            R_sum = query(right_node, mid+1, end)
            return L_sum + R_sum
        return query(0, 0, len(self.nums)-1)

class NumArrayIterative:

    def __init__(self, nums: List[int]):
        """
        T(n) = O(n) -- store all nodes and compute range sum
        S(n) = O(n) -- size of segment tree
        """
        if not nums:
            return None
        self.n = len(nums)
        self.stree = [0] * (2 * self.n)
        for i in range(self.n, 2 * self.n):
            self.stree[i] = nums[i - self.n]
        for i in range(self.n - 1, -1, -1):
            self.stree[i] = self.stree[2 * i] + self.stree[2 * i + 1]

    def update(self, i: int, val: int) -> None:
        """
        T(n) = O(logn) -- binary search in array to perform lazy update
        S(n) = O(1)
        """
        i += self.n
        self.stree[i] = val
        while i > 0:
            L = R = i
            if i % 2 == 0:
                R += 1
            else:
                L -= 1
            i //= 2
            self.stree[i] = self.stree[L] + self.stree[R]

    def sumRange(self, i: int, j: int) -> int:
        """
        T(n) = O(logn) -- binary search in array to find correct sum
        S(n) = O(1)
        """
        res = 0
        i += self.n
        j += self.n
        while i <= j:
            if i % 2 == 1:
                res += self.stree[i]
                i += 1
            if j % 2 == 0:
                res += self.stree[j]
                j -= 1
            i //= 2
            j //= 2
        return res

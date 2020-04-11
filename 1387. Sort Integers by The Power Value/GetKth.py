"""
The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

if x is even then x = x / 2
if x is odd then x = 3 * x + 1
For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

Return the k-th integer in the range [lo, hi] sorted by the power value.

Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1 using these steps and that the power of x is will fit in 32 bit signed integer.
"""
from heapq import heapify, heappop


class Solution:
    def __init__(self):
        self.mp = {}

    def getKth_heap_sort(self, lo: int, hi: int, k: int) -> int:
        """
        T(n) = O((n + k)logn) = n + nlogn + klogn
        S(n) = O(n)
        """
        pq = []
        for n in range(lo, hi + 1):
            pq.append((self.power(n), n))
        heapify(pq)
        while len(pq) - 1 > hi + 1 - lo - k:
            heappop(pq)
        return heappop(pq)[1]

    def getKth_double_sort(self, lo: int, hi: int, k: int) -> int:
        """
        T(n) = O(nlogn) = n + 2nlogn
        S(n) = O(n)
        """
        num_pow_dict = {}
        for n in range(lo, hi + 1):
            num_pow_dict[n] = self.power(n)
        return sorted(
            num_pow_dict.items(),
            key=lambda x: (
                x[1],
                x[0]))[
            k - 1][0]

    def power(self, n: int) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        if n == 1:
            return 0
        if n in self.mp:
            return self.mp[n]
        new_n = 0
        if n % 2 == 0:
            new_n = n // 2
        else:
            new_n = 3 * n + 1
        self.mp[n] = self.power(new_n) + 1
        return self.mp[n]

"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
"""
class Solution:
    def nthUglyNumber_heap(self, n: int) -> int:
        """
        T(n) = O(nlogn) -- push and pop costs logn and gets called n times
        S(n) = O(n)
        """
        from heapq import heappop, heappush
        q, seen, res = [1], set(), 1
        for _ in range(n):
            while res in seen:
                res = heappop(q)
            seen.add(res)
            for i in [2, 3, 5]:
                    heappush(q, res * i)
        return res

    def nthUglyNumber_3_ptrs(self, n: int) -> int:
        """
        T(n) = O(n) -- push and pop costs logn and gets called n times
        S(n) = O(n)
        """
        res = [1]
        i = j = k = 0
        while len(res) != n:
            cur_ugly = min(res[i] * 2, res[j] * 3, res[k] * 5)
            res.append(cur_ugly)
            if cur_ugly == res[i] * 2:
                i += 1
            if cur_ugly == res[j] * 3:
                j += 1
            if cur_ugly == res[k] * 5:
                k += 1
        return res[-1]
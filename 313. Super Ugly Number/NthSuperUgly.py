"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
"""


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        T(n) = O(nlogn) -- calls push and pop n times
        S(n) = O(n)
        """
        from heapq import heappop, heappush
        q, seen, res = [1], set(), 1
        for _ in range(n):
            while res in seen:
                res = heappop(q)
            seen.add(res)
            for i in primes:
                heappush(q, res * i)
        return res

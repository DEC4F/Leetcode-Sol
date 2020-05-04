"""
Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k, whether a Fibonacci number could be used multiple times.
"""


class Solution:
    def findMinFibonacciNumbers_rec(self, k: int) -> int:
        """
        T(n) = O(logk)
        S(n) = O(logk)
        """
        if k < 2:
            return k
        f1 = f2 = 1
        while f2 <= k:
            f1, f2 = f2, f1 + f2
        return self.findMinFibonacciNumbers(k - f1) + 1

    def findMinFibonacciNumbers_iter(self, k: int) -> int:
        """
        T(n) = O(logk)
        S(n) = O(1)
        """
        res = 0
        f1 = f2 = 1
        while f2 <= k:
            f1, f2 = f2, f1 + f2
        while f1 > 0:
            if f1 <= k:
                k -= f1
                res += 1
            f1, f2 = f2 - f1, f1
        return res
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.

Given N, calculate F(N).
"""


class Solution:
    def fib(self, N: int) -> int:
        """
        T(n) = O(log n) -- state trans matrix perform binary search
        S(n) = O(1)
        """
        import numpy as np
        return np.linalg.matrix_power(np.array([[1, 1], [1, 0]]), N)[0, 1]

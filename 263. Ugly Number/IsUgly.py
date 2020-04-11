"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
"""


class Solution:
    def isUgly(self, num: int) -> bool:
        """
        T(n) = O(logn)
        S(n) = O(1)
        """
        if num == 0:
            return False
        for n in [2, 3, 5]:
            while num % n == 0:
                num = num / n
        return num == 1

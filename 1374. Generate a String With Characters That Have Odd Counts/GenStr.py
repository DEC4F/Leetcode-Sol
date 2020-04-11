"""
Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        if n & 1:
            return 'x' * n
        return 'x' * (n - 1) + 'y'
"""
Given a 32-bit signed integer, reverse digits of an integer.
"""


class Solution:
    def reverse(self, x: int) -> int:
        """
        T(n) = O(D) -- num of digits
        S(n) = O(1)
        """
        res = 0
        max_int, min_int = (1 << 31) - 1, -1 << 31
        is_neg = x < 0
        x = abs(x)
        while x != 0:
            pop = x % 10
            x //= 10
            res = res * 10 + pop
            if not (min_int <= res <= max_int):
                return 0
        if is_neg:
            res = -res
        return res
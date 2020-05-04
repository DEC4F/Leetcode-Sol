"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
"""


class Solution:
    def rangeBitwiseAnd_keep_common_prefix(self, m: int, n: int) -> int:
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        shift = 0
        while m < n:
            n >>= 1
            m >>= 1
            shift += 1
        return m << shift

    def rangeBitwiseAnd_turnoff_one_bit(self, m: int, n: int) -> int:
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        while n > m:
            n &= n - 1
        return m & n
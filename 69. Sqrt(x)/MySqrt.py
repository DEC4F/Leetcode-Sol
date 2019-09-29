"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        T(n) = O(logn) -- binary search for sqrt
        S(n) = O(1)
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        l = 1
        r = x // 2
        while l <= r:
            mid = l + (r-l)//2
            sqrt = x // mid
            if mid == sqrt:
                return mid
            elif mid < sqrt:
                l = mid
            else:
                r = mid
        return r
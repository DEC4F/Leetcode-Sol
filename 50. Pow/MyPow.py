"""
Implement pow(x, n), which calculates x raised to the power n (xn).
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        T(n) = O(logn) -- reduce value of n by half each iteration
        S(n) = O(1) -- no extra array or recursion used
        """
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1.0
        while n:
            if n % 2 == 1:
                ans *= x
            x *= x
            n = n // 2

        return ans

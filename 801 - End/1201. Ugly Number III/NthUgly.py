"""
Write a program to find the n-th ugly number.

Ugly numbers are positive integers which are divisible by a or b or c.
"""
import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
        T(n) = 2logn = O(logn)
        S(n) = O(1)
        ----------
        m = count the numbers of multiples under num
          = also means num is the m-th ugly number
        """
        if a == 1 or b == 1 or c == 1:
            return n

        # def gcd(x: int, y: int) -> int:
        #   if y == 0:
        #       return x
        #   return gcd(y, x % y)

        # lcm(x,y) * gcd(x,y) = x * y
        lcm_ab = a * b // math.gcd(a, b)
        lcm_ac = a * c // math.gcd(a, c)
        lcm_bc = b * c // math.gcd(b, c)
        lcm_abc = lcm_ab * lcm_ac // math.gcd(lcm_ab, lcm_ac)

        lo, hi = 1, n * min(a, b, c)
        # search for the nth ugly number
        while lo < hi:
            mid = (lo + hi) // 2
            # mid is the m-th ugly number
            m = mid // a + mid // b + mid // c
            m -= mid // lcm_ab + mid // lcm_ac + mid // lcm_bc
            m += mid // lcm_abc
            if m == n:
                # int division
                return max(mid // a * a, mid // b * b, mid // c * c)
            elif m > n:
                hi = mid
            else:
                lo = mid + 1
        return lo

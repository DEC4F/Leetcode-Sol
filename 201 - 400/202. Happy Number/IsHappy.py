"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        T(n) = 2logn = O(logn) -- fast&slow ptr costs logn and get_next costs logn
        S(n) = O(1)
        """
        if not n:
            return False

        def get_next(num: int) -> int:
            res = 0
            while num > 0:
                num, digit = divmod(num, 10)
                res += digit ** 2
            return res
        t_ptr, h_ptr = n, get_next(n)
        while h_ptr != 1 and t_ptr != h_ptr:
            t_ptr = get_next(t_ptr)
            h_ptr = get_next(get_next(h_ptr))
        return h_ptr == 1

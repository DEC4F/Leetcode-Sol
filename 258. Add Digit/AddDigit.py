"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
"""
class Solution:
    def addDigits_iterative(self, num: int) -> int:
        """
        T(n) = O(logn)
        S(n) = O(1)
        """
        while num > 9:
            num, r = divmod(num, 10)
            num += r
        return num
    
    def addDigits_digital_roots(self, num: int) -> int:
        """
        T(n) = O(1)
        S(n) = O(1)
        ----------
        formula from https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
        res = 0                     if n  = 0
            = 1 + (n - 1) % (b - 1) if n != 0
        """
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
"""
Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.
"""


class Solution:
    def confusingNumber(self, N: int) -> bool:
        """
        T(n) = O(D) -- number of digits in the number
        S(n) = O(1)
        """
        rev = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        num, rev_num = N, 0
        while num:
            r = num % 10
            if r not in rev:
                return False
            rev_num = 10 * rev_num + rev[r]
            num //= 10
        return rev_num != N

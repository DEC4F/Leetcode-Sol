"""
Given a number s in their binary representation. Return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It's guaranteed that you can always reach to one for all testcases.
"""


class Solution:
    def numSteps_convert_to_base_10(self, s: str) -> int:
        """
        T(n) = O(n) -- suppose we have n bit (n char in the str), then it can represent any num in [1 - 2^n], the while loop would shrink the number by half, so thats log(2^n) = n. int func should also be O(n)
        S(n) = O(1)
        """
        n = int(s, base=2)
        res = 0
        while n != 1:
            if n & 1:
                n += 1
            else:
                n >>= 1
            res += 1
        return res

    def numSteps_str_comp(self, s: str) -> int:
        res = 0
        while s != '1':
            if s[-1] == '0':
                s = s[:-1] # right shift = divide by 2
            else:
                while s and s[-1] == '1':
                    res += 1
                    s = s[:-1] # right shift = carry
                s = s[:-1] + '1'
            res += 1        return res

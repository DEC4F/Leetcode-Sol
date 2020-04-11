"""
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        T(n) = O(a + b + c)
        S(n) = O(1)
        """
        res = ''
        A = B = C = 0
        for i in range(a + b + c):
            # greedily appends the char w max num that doesnt break the cond
            max_let = max(a, b, c)
            if (a == max_let and A != 2) or (
                    B == 2 and a > 0) or (C == 2 and a > 0):
                res += 'a'
                a -= 1
                A += 1
                B = C = 0
            elif (b == max_let and B != 2) or (A == 2 and b > 0) or (C == 2 and b > 0):
                res += 'b'
                b -= 1
                B += 1
                A = C = 0
            elif (c == max_let and C != 2) or (A == 2 and c > 0) or (B == 2 and c > 0):
                res += 'c'
                c -= 1
                C += 1
                A = B = 0
        return res

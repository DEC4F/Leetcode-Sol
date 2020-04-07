"""
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
"""


class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        """
        T(n) = O(A + B)
        S(n) = O(1)
        """
        res = ''
        a = b = 0
        for i in range(A + B):
            max_let = max(A, B)
            if b == 2 or (A == max_let and a != 2):
                res += 'a'
                A -= 1
                a += 1
                b = 0
            elif a == 2 or (B == max_let and b != 2):
                res += 'b'
                B -= 1
                b += 1
                a = 0
        return res
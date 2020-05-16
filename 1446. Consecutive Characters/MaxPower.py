"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.
"""


class Solution:
    def maxPower(self, s: str) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        i = res = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[i] == s[j]:
                j += 1
            res = max(res, j - i)
            i = j
        return res

"""
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.
"""


class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        T(n) = O(n)
        S(n) = O(n)
        ----------
        uses the pattern
        """
        n = len(s)
        pf_table = [0] * n
        i = 0
        for j in range(1, n):
            while i > 0 and s[i] != s[j]:
                i = pf_table[i - 1]
            if s[i] == s[j]:
                i += 1
                pf_table[j] = i
        return s[:pf_table[n - 1]]
"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
"""


class Solution:
    def removeVowels(self, S: str) -> str:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        v = ('a', 'e', 'i', 'o', 'u')
        return ''.join([c for c in S if c not in v])

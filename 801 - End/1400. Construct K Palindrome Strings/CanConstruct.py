"""
Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.

Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.
"""
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        T(n) = O(n)
        S(n) = O(1) -- only 26 letters
        """
        if k > len(s):
            return False
        C = Counter(s)
        n_leftover = 0
        for cnt in C.values():
            if cnt % 2 != 0:
                n_leftover += 1
        return n_leftover <= k

    def canConstruct_lee215(self, s: str, k: int) -> bool:
        """
        same as the other hash table method, but more pythonic and uses bit ops
        """
        return sum([cnt & 1 for cnt in Counter(s).values()]) <= k <= len(s)

"""
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
"""
from collections import defaultdict


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        res = mask = 0
        mp = defaultdict(int)
        # a -> 1st bit, e: 2nd bit, ... u: 5th bit
        for i, c in enumerate('aeiou'):
            mp[c] = 1 << i

        # keep record of the earliest occurrence idx of each mask
        seen = {0: -1}
        for i, c in enumerate(s):
            mask ^= mp[c]
            seen.setdefault(mask, i)
            res = max(res, i - seen[mask])
        return res

    def findTheLongestSubstring_lee215(self, s: str) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        ---------
        somehow slower probably due to find function
        """
        res = mask = 0
        seen = {0: -1}
        for i, c in enumerate(s):
            # equivalent to mp
            mask ^= 1 << ('aeiou'.find(c) + 1) >> 1
            seen.setdefault(mask, i)
            res = max(res, i - seen[mask])
        return res

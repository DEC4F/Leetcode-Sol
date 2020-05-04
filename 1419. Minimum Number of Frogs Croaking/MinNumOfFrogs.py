"""
Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.
"""


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        n_frog = res = 0
        mp = {}
        for c in 'croak':
            mp[c] = 0
        for c in croakOfFrogs:
            if c == 'c':
                n_frog += 1
                res = max(res, n_frog)
            elif c == 'k':
                n_frog -= 1
            mp[c] += 1
            if mp[c] > mp['c']:
                return -1
        if any(mp[c] != mp['c'] for c in mp.keys()):
            return -1
        return res
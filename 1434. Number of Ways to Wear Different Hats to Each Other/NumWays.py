"""
There are n people and 40 types of hats labeled from 1 to 40.

Given a list of list of integers hats, where hats[i] is a list of all hats preferred by the i-th person.

Return the number of ways that the n people wear different hats to each other.

Since the answer may be too large, return it modulo 10^9 + 7.
"""
from collections import defaultdict
from functools import lru_cache


class Solution:
    def __init__(self):
        self.n_caps = 40

    def numberWays(self, hats: List[List[int]]) -> int:
        """
        T(n) = O(c * 2^n)
        S(n) = O(c * 2^n)
        """
        @lru_cache(None)
        def dp(mask, hid):
            if mask == end_mask:
                return 1
            if hid > self.n_caps:
                return 0
            res = dp(mask, hid + 1)
            for pid in hp_mp[hid]:
                # if pid-th person doesn't has hat
                if mask & 1 << pid == 0:
                    res += dp(mask | 1 << pid, hid + 1) % mod
            return res % mod

        hp_mp = defaultdict(list)
        for pid, hs in enumerate(hats):
            for hid in hs:
                hp_mp[hid].append(pid)

        mod = 10 ** 9 + 7
        end_mask = (1 << len(hats)) - 1
        return dp(0, 0)
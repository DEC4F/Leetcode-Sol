"""
Given the strings s1 and s2 of size n, and the string evil. Return the number of good strings.

A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 10^9 + 7.
"""
from functools import lru_cache


class Solution:
    def numOfArrays_top_down(self, n: int, m: int, k: int) -> int:
        """
        T(n) = O(NMK)
        S(n) = O(NK)
        """
        @lru_cache(maxsize=None)
        def dp(i: int, h: int, c: int) -> int:
            if i == n and c == k:
                return 1
            if i == n or c > k:
                return 0
            res = 0
            for j in range(1, m + 1):
                res += dp(i + 1, max(h, j), c + (j > h))
            return res
        return dp(0, 0, 0) % (10 ** 9 + 7)

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
        T(n) = O(NMK)
        S(n) = O(NK)
        """
        # 3 matrices of size (n + 1, k + 1)
        maxs, P1, P2 = [[[0] * (n + 1) for _ in range(k + 1)]
                        for _ in range(3)]
        for cur_max in range(1, m + 1):
            for L in range(1, n + 1):
                for cost in range(1, min(k, cur_max, L) + 1):
                    if cost == L == 1:
                        maxs[1][1] = 1
                    else:
                        maxs[cost][L] = P2[cost - 1][L - 1] + \
                            maxs[cost][L - 1] * cur_max
                    P1[cost][L] = maxs[cost][L] + P2[cost][L]
            P2 = [row[:] for row in P1]

        return P1[-1][-1] % (10 ** 9 + 7)

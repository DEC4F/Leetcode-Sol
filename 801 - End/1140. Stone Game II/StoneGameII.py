"""
Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.
"""
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        T(n) = O(n^2)
        S(n) = O(n^2)
        """
        N = len(piles)
        # converting to suffix sum array
        for i in range(N - 2, -1, -1):
            piles[i] += piles[i + 1]

        @lru_cache(None)
        def dp(i, m) -> int:
            # greedily take all stones if we can reach the end in one round
            if i + 2 * m >= N:
                return piles[i]
            # else, minimize the max gain of enemy
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return dp(0, 1)
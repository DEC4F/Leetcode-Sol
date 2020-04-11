"""
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.
"""
from functools import lru_cache


class Solution:
    def stoneGame_DP(self, piles: List[int]) -> bool:
        n = len(piles)

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for size in range(1, n + 1):
            for i in range(n + 1 - size):
                j = i + size - 1
                diff = (j + i + n) % 2
                if diff == 1:
                    dp[i + 1][j + 1] = max(dp[i + 2][j + 1] +
                                           piles[i], dp[i + 1][j] + piles[j])
                else:
                    dp[i + 1][j + 1] = min(dp[i + 2][j + 1] -
                                           piles[i], dp[i + 1][j] - piles[j])

        return dp[1][n] > 0

    def stoneGame_memo(self, piles: List[int]) -> bool:
        """
        T(n) = O(n^2)
        S(n) = O(n^2)
        """
        n = len(piles)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            turn = (n - (i + j)) % 2
            if turn == 1:  # ALEX playing
                return max(dp(i + 1, j) + piles[i], dp(i, j - 1) + piles[j])
            else:  # LEE playing
                return min(dp(i + 1, j) - piles[i], dp(i, j - 1) - piles[j])

        return dp(0, n - 1) > 0

    def stoneGame_math(self, piles: List[int]) -> bool:
        """
        for n = 4:
        alex can choose 1st & 3rd or 2nd & 4th, whichever is greater
        for n = k:
        alex can choose 1st & 3rd & ... k - 1th piles, or 2nd & 4th & ... kth piles, one of the two is greater, and the choice is in Alex's hands
        So alex (first player) always wins
        """
        return True

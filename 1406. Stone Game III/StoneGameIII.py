"""
Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2 or 3 stones from the first remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.
"""


class Solution:
    def stoneGameIII_1D_DP(self, stoneValue: List[int]) -> str:
        """
        T(n) = O(N)
        S(n) = O(N)
        """
        N = len(stoneValue)
        dp = [0] * (N + 1)
        for i in range(N - 1, -1, -1):
            dp[i] = float('-inf')
            take = 0
            for j in range(3):
                if i + j < N:
                    take += stoneValue[i + j]
                    dp[i] = max(dp[i], take - dp[i + j + 1])

        if dp[0] > 0:
            return 'Alice'
        if dp[0] < 0:
            return 'Bob'
        return 'Tie'

    def stoneGameIII_const_space(self, stoneValue: List[int]) -> str:
        """
        T(n) = O(N)
        S(n) = O(1)
        """
        N = len(stoneValue)
        dp = [0] * 3
        for i in range(N - 1, -1, -1):
            dp[i % 3] = max(sum(stoneValue[i:i + k]) - dp[(i + k) % 3]
                            for k in range(1, 4))

        if dp[0] > 0:
            return 'Alice'
        if dp[0] < 0:
            return 'Bob'
        return 'Tie'

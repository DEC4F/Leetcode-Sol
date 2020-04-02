"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        T(n) = O(N * C) -- number of amount and number of coins
        S(n) = O(N)
        """
        if not amount:
            return 1
        if not coins:
            return 0
        dp = [0] * (amount + 1)  # dp array of (amount : how many ways)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[amount]

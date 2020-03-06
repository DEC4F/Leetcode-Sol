"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        dp = [0]*(amount + 1)
        for i in range(1, amount + 1):
            dp[i] = min([float('inf')] + [dp[i - c] + 1 for c in coins if i >= c])
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

"""
Given an array of integers cost and an integer target. Return the maximum integer you can paint under the following rules:

The cost of painting a digit (i+1) is given by cost[i] (0 indexed).
The total cost used must be equal to target.
Integer does not have digits 0.
Since the answer may be too large, return it as string.

If there is no way to paint any integer given the condition, return "0".
"""
from functools import lru_cache


class Solution:
    def largestNumber_TD(self, cost: List[int], target: int) -> str::
        """
        T(n) = O(target)
        S(n) = O(target)
        """
        @lru_cache(None)
        def dp(i, r):
            if i == 9 or r < 0:
                return float('-inf')
            if r == 0:
                return 0
            return max(dp(i, r - cost[i]) * 10 + (i + 1), dp(i + 1, r))
        return str(max(dp(0, target), 0))

    def largestNumber_BU(self, cost: List[int], target: int) -> str:
        """
        T(n) = O(target)
        S(n) = O(target)
        """
        dp = [0] + [-1] * (target + 5000) # why 5000
        for r in range(1, target + 1):
            dp[r] = max(dp[r - c] * 10 + i + 1 for i, c in enumerate(cost))
        return str(max(dp[target], 0))

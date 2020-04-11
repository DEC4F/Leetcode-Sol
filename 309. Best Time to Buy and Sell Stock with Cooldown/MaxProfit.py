"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
"""


class Solution:
    def maxProfit_DP(self, prices: List[int]) -> int:
        """
        T(n) = n = O(n) -- one pass
        S(n) = 3n = O(n) -- 3 states transition matrix
        """
        n = len(prices)
        hold = [float('-inf')] * (n + 1)
        sold = [0] * (n + 1)
        rest = [0] * (n + 1)
        for i in range(1, n + 1):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i - 1])
            sold[i] = hold[i - 1] + prices[i - 1]
            rest[i] = max(rest[i - 1], sold[i - 1])
        return max(rest[n], sold[n])

    def maxProfit_DP_space_opt(self, prices: List[int]) -> int:
        """
        T(n) = O(n) -- one pass
        S(n) = O(1) -- only 4 vars used
        """
        hold = float('-inf')
        sold = 0
        rest = 0
        for p in prices:
            prev_sold = sold
            sold = hold + p
            hold = max(hold, rest - p)
            rest = max(rest, prev_sold)
        return max(rest, sold)

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        min_val = None
        max_profit = -1
        for p in prices:
            if min_val is None:
                min_val = p

            if p < min_val:
                min_val = p
            elif p - min_val > max_profit:
                max_profit = p - min_val

        return 0 if max_profit < 0 else max_profit

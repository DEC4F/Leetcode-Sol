"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
"""
class Solution:
    def maxProfit_find_pair(self, prices: List[int]) -> int:
        """
        T(n) = O(n) -- visiting each price exactly once
        S(n) = O(1)
        ----------
        greedily finding the (lo, hi) pair and add the diff to profit
        """
        n = len(prices)
        if n < 1:
            return 0
        lo = hi = prices[0]
        max_profit = 0
        i = 0
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            lo = prices[i]
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            hi = prices[i]
            max_profit += hi - lo
        return max_profit

    def maxProfit_one_for_loop(self, prices: List[int]) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        ----------
        similar to the above approach, but only with one for loop
        since if a < b < c, then (b - a) + (c - b) = (c - a) by continuity
        """
        n = len(prices)
        if n < 1:
            return 0
        max_profit = 0
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                max_profit += diff
        return max_profit

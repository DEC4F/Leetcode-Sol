"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
from math import factorial as fact


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        return fact(m + n - 2) // (fact(m - 1) * fact(n - 1))

    def uniquePaths_two_d(self, m: int, n: int) -> int:
        """
        T(n) = O(mn) -- travered entire grid
        S(n) = O(mn) -- used 2d array to store
        """
        if m < 0 or n < 0:
            return 0
        if m == 1 and n == 1:
            return 1
        ans = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
        return ans[m - 1][n - 1]

    def uniquePaths_one_d(self, m: int, n: int) -> int:
        """
        T(n) = O(mn) -- travered entire grid
        S(n) = O(n) -- used 1d array to store
        """
        if m < 0 or n < 0:
            return 0
        if m == 1 and n == 1:
            return 1
        ans = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # ans[j-1] is the ans[i][j-1] (top num), and ans[j] is the
                # ans[i-1][j] (left num)
                ans[j] += ans[j - 1]
        return ans[n - 1]

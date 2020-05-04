"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.
"""
from functools import lru_cache


class Solution:
    def longestCommonSubsequence_memo(self, text1: str, text2: str) -> int:
        """
        T(n) = O(MN)
        S(n) = O(MN)
        ----------
        dp[i, j] = 1 + dp[i + 1, j + 1]             if t[i] = t[j]
                 = max(dp[i + 1, j], dp[i, j + 1])  otherwise
        """
        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dp(i + 1, j + 1)
            return max(dp(i, j + 1), dp(i + 1, j))
        return dp(0, 0)

    def longestCommonSubsequence_BU_2D(self, text1: str, text2: str) -> int:
        """
        T(n) = O(MN)
        S(n) = O(MN)
        """
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]

    def longestCommonSubsequence_BU_1D(self, text1: str, text2: str) -> int:
        """
        T(n) = O(MN)
        S(n) = O(M)
        """
        if len(text2) > len(text1):
            return self.longestCommonSubsequence(text2, text1)
        n, m = len(text1), len(text2)
        prev_col = [0] * (m + 1)
        for i in range(n - 1, -1, -1):
            cur_col = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    cur_col[j] = 1 + prev_col[j + 1]
                else:
                    cur_col[j] = max(prev_col[j], cur_col[j + 1])
            prev_col = cur_col
        return prev_col[0]

class Solution:
    def maximalSquare_2d_dp(self, matrix: List[List[str]]) -> int:
        """
        T(n) = O(mn)
        S(n) = O(mn)
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
        return res ** 2

    def maximalSquare_1d_sq(self, matrix: List[List[str]]) -> int:
        """
        T(n) = O(mn)
        S(n) = O(m)
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [0] * (m + 1)
        res = top_left = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j], dp[j - 1], top_left) + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
                top_left = temp
        return res ** 2

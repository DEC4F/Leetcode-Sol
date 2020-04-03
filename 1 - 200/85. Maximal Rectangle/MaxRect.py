"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
"""


class Solution:
    def maximalRectangle_DP(self, matrix: List[List[str]]) -> int:
        pass

    def maximalRectangle_convert_to_histogram(
            self, matrix: List[List[str]]) -> int:
        """
        T(n) = O(NM) = NM + M -- building up heights histogram and search max area
        T(n) = O(M) -- size of histogram/stack
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return 0

        def maximal_histogram(heights: List[int]) -> int:
            """
            T(n) = O(M)
            T(n) = O(M)
            ----------
            solution to problem 84
            """
            res = 0
            stack = [-1]
            for i, h in enumerate(heights):
                while stack[-1] != -1 and h <= heights[stack[-1]]:
                    area = heights[stack.pop()] * (i - stack[-1] - 1)
                    res = max(res, area)
                stack.append(i)
            while stack[-1] != -1:
                area = heights[stack.pop()] * (len(heights) - stack[-1] - 1)
                res = max(res, area)
            return res

        res = 0
        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            res = max(res, maximal_histogram(heights))
        return res

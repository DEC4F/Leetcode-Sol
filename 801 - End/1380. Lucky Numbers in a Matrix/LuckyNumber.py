"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
"""


class Solution:
    def luckyNumbers_BF (self, matrix: List[List[int]]) -> List[int]:
        """
        T(n) = O(mn) = 2mn
        S(n) = O(n)
        """
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        row_min = {}
        for i in range(m):
            row_min[i] = min(matrix[i])
        for j in range(n):
            max_val, max_idx = float('-inf'), -1
            for i in range(m):
                if matrix[i][j] > max_val:
                    max_val = matrix[i][j]
                    max_idx = i
            if row_min[max_idx] == max_val:
                res.append(max_val)
        return res

    def luckyNumbers_set_diff (self, matrix: List[List[int]]) -> List[int]:
        """
        T(n) = O(mn) = 2mn
        S(n) = O(m + n)
        """
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]
        return list(set(row_min) & set(col_max))

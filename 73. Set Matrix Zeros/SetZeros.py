"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        T(n) = O(mn) -- traversed entire matrix
        S(n) = O(1) -- no extra space used
        """
        n = len(matrix) # n_row
        m = len(matrix[0]) # n_col
        first_col_is_zero = False
        for i in range(n):
            if matrix[i][0] == 0: # if any first element in a row is 0, then first col should be all 0
                first_col_has_zero = True
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0: # set first row to be zero if first cell is turned into 0
            for j in range(m):
                matrix[0][j] = 0
        if first_col_has_zero: # set first columns to be zero if previously marked as containing 0
            for i in range(n):
                matrix[i][0] = 0
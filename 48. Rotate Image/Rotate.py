"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
"""


class Solution:
    def rotate_transpose(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        T(n) = O(n^2) -- read all value in the matrix in transposing
        S(n) = O(1) -- const space
        """
        n = len(matrix)
        # take transpose
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        # reverse row (swapping columns)
        for r in matrix:
            r.reverse()

    def rotate_swap(self, matrix: List[List[int]]) -> None:
        """
        T(n) = n*n = O(n^2) -- two nested for loops
        S(n) = O(1) -- only used one temp variable
        """
        n = len(matrix[0])
        for r in range(n // 2 + n % 2):
            for c in range(n // 2):
                tmp = matrix[n - 1 - c][r]
                matrix[n - 1 - c][r] = matrix[n - 1 - r][n - 1 - c]
                matrix[n - 1 - r][n - 1 - c] = matrix[c][n - 1 - r]
                matrix[c][n - 1 - r] = matrix[r][c]
                matrix[r][c] = tmp

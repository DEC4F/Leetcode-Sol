"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""


class Solution:
    def searchMatrix_bi_search(self,
                               matrix: List[List[int]],
                               target: int) -> bool:
        """
        T(n) = O(logm + logn + mlogn) -- two binary searches and m binary searches for all valid rows
        S(n) = O(1)
        """
        if not matrix or not matrix[0] or target < matrix[0][0]:
            return False
        m, n = len(matrix), len(matrix[0])

        def bound(l, r, is_row):
            while l < r:
                mid = (l + r) // 2
                if is_row:
                    if matrix[mid][0] < target:
                        l = mid + 1
                    else:
                        r = mid
                else:
                    if matrix[0][mid] < target:
                        l = mid + 1
                    else:
                        r = mid
            return l

        row_bound, col_bound = bound(0, m - 1, True), bound(0, n - 1, False)

        def b_search(row, l, r):
            while l < r:
                mid = (l + r) // 2
                if matrix[row][mid] == target:
                    return mid
                if matrix[row][mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return -1

        for r in range(row_bound + 1):
            c = b_search(r, 0, col_bound + 1)
            if c != -1:
                return True
        return False

    def searchMatrix_div_n_conquer(self,
                                   matrix: List[List[int]],
                                   target: int) -> bool:
        """
        T(n) = O(nlogn)
        S(n) = O(1)
        """
        if not matrix or not matrix[0]:
            return False

        def rec(u: int, d: int, l: int, r: int) -> bool:
            if l > r or u > d:
                return False
            if target < matrix[u][l] or target > matrix[d][r]:
                return False

            mid = (l + r) // 2
            row = u
            while row <= d and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            # bottom left submat or top right submat
            return rec(row, d, l, mid - 1) or rec(u, row - 1, mid + 1, r)

        return rec(0, len(matrix) - 1, 0, len(matrix[0]) - 1)

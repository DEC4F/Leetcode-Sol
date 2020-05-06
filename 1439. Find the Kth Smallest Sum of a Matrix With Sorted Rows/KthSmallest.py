"""
You are given an m * n matrix, mat, and an integer k, which has its rows sorted in non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return the Kth smallest array sum among all possible arrays.
"""


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        """
        T(n) = O(m*n^2log(n)) --- sort a n^2 list takes O(n^2logn) time, do it m times (n_rows)
        S(n) = O(n^2)
        """
        h = mat[0][:]
        for row in mat[1:]:
            sums = [i + j for i in row for j in h] #m^2
            h = sorted(sums)[:k]
        return h[k - 1]
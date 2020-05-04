"""
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        T(n) = O(MN)
        S(n) = O(1)
        """
        n, m = binaryMatrix.dimensions()
        i, j = 0, m - 1
        res = m
        flg = False
        while i <= n - 1 and j >= 0:
            if binaryMatrix.get(i, j) == 1:
                flg = True
                res = min(res, j)
                j -= 1
            else:
                i += 1
        return res if flg else -1

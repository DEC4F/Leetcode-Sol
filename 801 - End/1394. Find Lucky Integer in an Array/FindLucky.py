"""
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
"""
import collections


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        T(n) = O(n) = 2n
        S(n) = O(n)
        """
        res = -1
        c = collections.Counter(arr)
        for k, v in c.items():
            if k == v:
                res = max(res, k)
        return res

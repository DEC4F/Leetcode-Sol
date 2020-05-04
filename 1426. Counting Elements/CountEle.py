"""
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.
"""
from collections import Counter


class Solution:
    def countElements(self, arr: List[int]) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        mp = Counter(arr)
        res = 0
        for n in mp.keys():
            if mp[n + 1] > 0:
                res += mp[n]
        return res
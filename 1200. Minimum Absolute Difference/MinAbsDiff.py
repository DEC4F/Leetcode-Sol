"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

- a, b are from arr
- a < b
- b - a equals to the minimum absolute difference of any two elements in arr
"""


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        T(n) = O(nlogn) = nlogn + n
        S(n) = O(1)
        """
        if not arr or len(arr) <= 1:
            return []
        arr.sort()
        diff = float('inf')
        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < diff:
                diff = arr[i] - arr[i - 1]
                res = [[arr[i - 1], arr[i]]]
            elif arr[i] - arr[i - 1] == diff:
                res.append([arr[i - 1], arr[i]])
        return res
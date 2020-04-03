"""
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
"""


class Solution:
    def findTheDistanceValue_BF(self, arr1: List[int],
                                arr2: List[int], d: int) -> int:
        """
        T(n) = O(n^2)
        S(n) = O(1)
        """
        res = 0
        for n1 in arr1:
            valid = True
            for n2 in arr2:
                if abs(n1 - n2) <= d:
                    valid = False
                    break
            if valid:
                res += 1
        return res

    def findTheDistanceValue_bisect(self, arr1: List[int],
                                    arr2: List[int], d: int) -> int:
        """
        T(n) = O(nlogn)
        S(n) = O(1)
        """
        res = 0
        arr2.sort()
        for n in arr1:
            i = bisect.bisect(arr2, n)
            if (0 <= i < len(arr2) and abs(n - arr2[i]) <= d) or (0 <= i - 1 < len(arr2) and abs(n - arr2[i - 1]) <= d):
                continue
            res += 1
        return res
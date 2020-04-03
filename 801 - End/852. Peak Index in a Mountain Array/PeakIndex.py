"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
"""


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        """
        T(n) = O(logn) -- binary search
        S(n) = O(1)
        """
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] < A[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l

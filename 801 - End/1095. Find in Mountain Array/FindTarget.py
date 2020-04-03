"""
(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.
"""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:

    def __init__(self):
        self.cache = {}

    def findInMountainArray(
            self,
            target: int,
            mountain_arr: 'MountainArray') -> int:
        """
        T(n) = O(logn) = logn + 1/2logn + 1/2logn -- one binary search and two halves binary search
        S(n) = O(n) -- size of cache
        """
        n = mountain_arr.length()
        peak = self.peak_idx(n, mountain_arr)
        left_res = self.target_idx(0, peak, target, mountain_arr, True)
        if left_res != -1:
            return left_res
        return self.target_idx(peak, n - 1, target, mountain_arr, False)

    def get(self, mountain_arr, i):
        """
        T(n) = O(1)
        S(n) = O(n)
        """
        if self.cache.get(i) is None:
            self.cache[i] = mountain_arr.get(i)
        return self.cache[i]

    def peak_idx(self, n: int, mountain_arr: 'MountainArray') -> int:
        """
        T(n) = O(logn)
        S(n) = O(1)
        """
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if self.get(mountain_arr, mid) < self.get(mountain_arr, mid + 1):
                l = mid + 1
            else:
                r = mid
        return l

    def target_idx(
            self,
            l: int,
            r: int,
            target: int,
            mountain_arr: 'MountainArray',
            is_inc: bool) -> int:
        """
        T(n) = O(logn)
        S(n) = O(1)
        """
        while l < r:
            mid = (l + r) // 2
            mid_val = self.get(mountain_arr, mid)
            if mid_val == target:
                return mid
            if (mid_val < target) == is_inc:
                l = mid + 1
            else:
                r = mid
        if self.get(mountain_arr, l) == target:
            return l
        return -1

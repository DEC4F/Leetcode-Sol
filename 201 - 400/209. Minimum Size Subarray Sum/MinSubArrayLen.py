"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        T(n) = O(n) -- each n may be visited at most 2 times
        S(n) = O(1)
        """
        l = 0
        total = 0
        res = float('inf')
        for r, n in enumerate(nums):
            total += n
            while total >= s:
                res = min(res, r + 1 - l)
                total -= nums[l]
                l += 1
        if res == float('inf'):
            return 0
        return res

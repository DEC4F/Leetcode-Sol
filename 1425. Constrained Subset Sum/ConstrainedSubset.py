"""
Given an integer array nums and an integer k, return the maximum sum of a non-empty subset of that array such that for every two consecutive integers in the subset, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subset of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.
"""
from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        dp = [nums[0]]  # dp[i] = max sum from nums[:i] & include nums[i]
        dec_dq = deque(dp)  # non-inc, records max in (dp[i - k:i])
        for i, n in enumerate(nums[1:], 1):
            if i > k and dec_dq[0] == dp[i - k - 1]:
                dec_dq.popleft()
            tmp = max(n, dec_dq[0] + n)
            dp.append(tmp)
            while dec_dq and dec_dq[-1] < tmp:
                dec_dq.pop()
            dec_dq.append(tmp)
        return max(dp)

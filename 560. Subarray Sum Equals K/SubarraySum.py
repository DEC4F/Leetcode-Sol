"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
"""
from collections import defaultdict


class Solution:
    def subarraySum_cum_sum(self, nums: List[int], k: int) -> int:
        """
        T(n) = n + n^2 = O(n^2) -- calculated difference btwn each pair
        S(n) = O(n) -- cum sum array
        """
        ans = 0
        cum_sum = [0] * (len(nums) + 1)
        cum_sum[0] = 0
        for i in range(1, len(nums) + 1):
            cum_sum[i] = cum_sum[i - 1] + nums[i - 1]
        for l in range(len(nums)):
            for r in range(l + 1, len(nums) + 1):
                if (cum_sum[r] - cum_sum[l]) == k:
                    ans += 1
        return ans

    def subarraySum_range_sum(self, nums: List[int], k: int) -> int:
        """
        T(n) = n + n^2 = O(n^2) -- calculated difference btwn each pair
        S(n) = O(1) -- no extra var
        """
        ans = 0
        for l in range(len(nums)):
            range_sum = 0
            for r in range(l, len(nums)):
                range_sum += nums[r]
                if range_sum == k:
                    ans += 1
        return ans

    def subarraySum_hash(self, nums: List[int], k: int) -> int:
        """
        T(n) = O(n) -- one pass to build cum sum dict and compute answer on the fly
        S(n) = O(n) -- cum sum dict
        """
        ans = 0
        mp = defaultdict(int)
        s = 0
        mp[s] = 1
        for i in range(len(nums)):
            s += nums[i]
            if mp[s - k] != 0:
                ans += mp[s - k]
            mp[s] += 1
        return ans

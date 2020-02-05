"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
"""

class Solution:
    def subarraySum_cum_sum(self, nums: List[int], k: int) -> int:
        """
        T(n) = n + n^2 = O(n^2) -- calculated difference btwn each pair
        S(n) = O(n) -- cum sum array
        """
        ans = 0
        cum_sum = [0]*(len(nums)+1)
        cum_sum[0] = 0
        for i in range(1, len(nums)+1):
            cum_sum[i] = cum_sum[i-1] + nums[i-1]
        for l in range(len(nums)):
            for r in range(l+1, len(nums)+1):
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
        sum_count_map = {0 : 1}
        cum_sum = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum-k in sum_count_map.keys():
                ans += sum_count_map[cum_sum-k]

            if cum_sum in sum_count_map.keys():
                sum_count_map[cum_sum] += 1
            else:
                sum_count_map[cum_sum] = 1
            
        return ans
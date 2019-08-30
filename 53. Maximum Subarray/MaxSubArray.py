"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

class Solution:
    def maxSubArray_DP(self, nums: List[int]) -> int:
        """
        T(n) = O(n) -- one pass
        S(n) = O(1) -- used two extra var
        ----------
        Note: this is also greedy
        """
        ans = nums[0]
        subarr_sum = nums[0]
        for i in range(1, len(nums)):
            subarr_sum = max(subarr_sum + nums[i], nums[i])
            if ans < subarr_sum:
                ans = subarr_sum
        return ans

    def maxSubArray_DC(self, nums: List[int]) -> int:
        """
        T(n)
        S(n)
        """
        pass

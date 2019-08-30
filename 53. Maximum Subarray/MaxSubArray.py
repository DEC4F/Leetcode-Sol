"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)
        
    def helper(self, nums: List[int], l: int, r: int) -> int:
        """
        T(n) = 2T(n/2) + cn = O(nlogn) -- by master theorem case 2
        S(n) = O(logn) -- recursion stack
        """
        if l == r:
            return nums[l]
        mid = (l+r)//2
        left_max = self.helper(nums, l, mid) # T(n/2)
        right_max = self.helper(nums, mid+1, r) # T(n/2)
        crossing_max = self.maxCrossingSubArray(nums, l, r, mid) # O(n)
        return max(left_max, right_max, crossing_max)
    
    def maxCrossingSubArray(self, nums: List[int], l: int, r: int, mid: int) -> int:
        l_max_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, l-1, -1):
            curr_sum += nums[i]
            l_max_sum = max(curr_sum, l_max_sum)
        
        r_max_sum = float('-inf')
        curr_sum = 0
        for i in range(mid+1, r+1):
            curr_sum += nums[i]
            r_max_sum = max(curr_sum, r_max_sum)
        
        return l_max_sum + r_max_sum
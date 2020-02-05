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

    def maxSubArray_DC(self, nums: List[int], lo: int, hi: int) -> int:
        """
        T(n) = 2T(n/2) + cn = O(nlogn) by master theoream case 2
        S(n) = O(logn) -- recursion stack size, splitted in half each level
        """
        if lo == hi:
            return nums[lo]
        mid = (hi+lo)//2
        max_left = self.maxSubArray_DC(nums, lo, mid)
        max_right = self.maxSubArray_DC(nums, mid+1, hi)
        max_crossing = self.maxCrossingSubArray(nums, lo, mid, hi)
        return max(max_left, max_right, max_crossing)
    
    def maxCrossingSubArray(self, nums:List[int], lo: int, mid: int, hi: int) -> int:
        """
        T(n) = O(n)
        """
        left_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, lo-1, -1):
            curr_sum += nums[i]
            left_sum = max(curr_sum, left_sum)

        right_sum = float('-inf')
        curr_sum = 0
        for i in range(mid+1, hi+1):
            curr_sum += nums[i]
            right_sum = max(curr_sum, right_sum)

        return right_sum + left_sum
    
    def maxSubArray_compare(self, nums: List[int], lo, hi) -> List[int]:
        """
        T(n) = 2T(n/2) + d = O(n) -- finding max crossing subarray is reduced to constant time, by master theorem case 2 we have O(n)
        S(n) = O(log n) -- recursion stack size, splitted in even halves in each level
        """
        if lo == hi:
            return [nums[lo], nums[lo], nums[lo], nums[lo]]
        mid = (hi+lo)//2
        left = self.MS_compare(nums, lo, mid)
        right = self.MS_compare(nums, mid+1, hi)
        return self.compare(nums, left, right)
    
    def compare(self, nums:List[int], L: List[int], R: List[int]) -> int:
        """
        T(n) = O(1) -- const time in comparison
        S(n) = O(1) -- const space used

        L = [left_totalSum, left_maxPrefix, left_maxSuffix, left_maxSum]
        R = [right_totalSum, right_maxPrefix, right_maxSuffix, right_maxSum]
        """
        totalSum = L[0] + R[0]
        maxPrefix = max(L[1], L[0]+R[1]) # max(left_maxPrefix, left_totalSum+right_maxPrefix)
        maxSuffix = max(R[2], R[0]+L[2]) # max(right_maxSuffix, right_totalSum+left_maxSuffix)
        maxSum = max(L[3], R[3], L[2]+R[1]) # max(leftMax, rightMax, leftSuffix+rightPrefix)
        return [totalSum, maxPrefix, maxSuffix, maxSum]
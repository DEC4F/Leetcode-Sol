"""
Given an unsorted array of integers, find the number of longest increasing subsequence.
"""

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        T(n) = n*n = O(n^2) -- two loops finding LIS ending at nums[i]
        S(n) = 2n = O(n) -- two arrays used
        ----------
        note:
            we examine the LIS ending at index i
            if it's greater than the predecessor nums[j], then we checks if the LIS ending at j is greater than the current LIS length found at i
            if so, we add i to the LIS and inherit the LIS count
            else if len of LIS ending at j is exactly 1 less than that of i, we just increment count[i] by count[j]
        """
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return 1
        LIS_count = [1]*n
        LIS_len = [0]*n
        
        # compute LIS ending at nums[i]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if LIS_len[j] >= LIS_len[i]:
                        LIS_len[i] = LIS_len[j] + 1
                        LIS_count[i] = LIS_count[j]
                    elif LIS_len[i] == LIS_len[j] + 1:
                        LIS_count[i] += LIS_count[j]
        LIS = max(LIS_len)
        return sum(c for i, c in enumerate(LIS_count) if LIS_len[i] == LIS)
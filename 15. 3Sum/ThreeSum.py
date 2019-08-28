"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        T(n) = O(n^2)
        S(n) = O(n^2) -- use (n-2) dict to store compliments of (n-1) numbers
        """
        if len(nums) < 3:
            return []
        results = set()
        nums.sort()
        for i, n in enumerate(nums[:-2]):
            if i > 0 and n == nums[i-1]:
                continue
            comps = {}
            for m in nums[i+1:]:
                c = -n - m
                if m not in comps:
                    comps[c] = 1
                else:
                    results.add((n, c, m))

        return list(results)

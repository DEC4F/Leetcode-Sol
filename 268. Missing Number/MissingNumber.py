"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""

class Solution:

    def missingNumber_list(self, nums: List[int]) -> int:
        """
        T(n) = 3n = O(n) -- build list, verify, and indexing takes O(n) time each
        S(n) = O(n) -- size of list
        """
        if not nums or len(nums) == 0:
            return -1
        seen = [1]*(len(nums)+1)
        for n in nums:
            seen[n] -= 1
        return seen.index(1)

    def missingNumber_sum(self, nums: List[int]) -> int:
        """
        T(n) = O(n) -- sum takes O(n) time
        S(n) = O(1) -- no extra space used
        """
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum-actual_sum

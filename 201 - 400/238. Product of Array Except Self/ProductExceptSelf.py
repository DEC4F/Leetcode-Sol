"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        T(n) = O(n) -- two passes, one to get the cum prod of the left hand side, and one to calc the total prod
        S(n) = O(n) -- answers array
        """
        L = [0] * len(nums)
        R = 1

        L[0] = 1
        for i in range(1, len(nums)):
            L[i] = L[i - 1] * nums[i - 1]

        for i in reversed(range(len(nums))):
            L[i] = L[i] * R
            R *= nums[i]

        return L

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""


class Solution:
    def moveZeroes_original(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        T(n) = O(n)
        S(n) = O(1)
        ---------
        somehow this is faster than the shorter solution, despite same logic
        """
        # i is the 0-ptr, j is the non-0-ptr
        i = j = 0
        while i < len(nums):
            # inc non zero ptr
            while i < len(nums) and nums[i] == 0:
                i += 1
            # inc zero ptr
            while j < len(nums) and nums[j] != 0:
                j += 1
            # swap if 0 is on the left of non-0 ele
            if j < i and i < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
            i += 1

    def moveZeroes_lc_sol(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        T(n) = O(n)
        S(n) = O(1)
        """
        # i is the non-0-ptr, j is the 0-ptr
        i = j = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1

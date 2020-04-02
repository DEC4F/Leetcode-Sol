"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        T(n) = O(n) -- one pass
        S(n) = O(1) -- used only 3 vars
        """
        if len(nums) == 0 or nums is None:
            return nums
        if len(nums) == 1:
            return nums[0]
        max_prod = nums[0]
        curr_max_prod = nums[0]
        curr_min_prod = nums[0]
        for i in range(1, len(nums)):
            temp = curr_max_prod
            curr_max_prod = max(
                curr_max_prod * nums[i],
                curr_min_prod * nums[i],
                nums[i])
            curr_min_prod = min(
                curr_min_prod * nums[i],
                temp * nums[i],
                nums[i])
            max_prod = max(max_prod, curr_max_prod)
        return max_prod

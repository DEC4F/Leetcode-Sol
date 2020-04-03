"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        T(n) = 3n = O(n) -- three passes in worst case
        S(n) = O(1) -- no extra spaced used
        """
        # find first dec element n_i
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:  # O(n)
            i -= 1
        if i >= 0:
            # find num n_j that is just larger than n_i
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:  # O(n)
                j -= 1
            # swap them
            nums[i], nums[j] = nums[j], nums[i]

        # reverse array to the right of n_j
        i += 1
        j = len(nums) - 1
        while i < j:  # O(n)
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

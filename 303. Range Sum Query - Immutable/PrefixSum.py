"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
"""
class NumArray:

    def __init__(self, nums: List[int]):
        """
        T(n) = O(n) -- compute all prefix sum
        S(n) = O(n) -- size of sum array
        """
        if len(nums) > 0:
            self.prefix_sum = [0]
            for i in range(len(nums)):
                self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        return self.prefix_sum[j + 1] - self.prefix_sum[i]

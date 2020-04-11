"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        use hashmap to look up complement (target - curr_num) of each number
        T = O(n)
        S = O(n)
        """
        counterparts = {}
        for i, curr_num in enumerate(nums):
            complement = target - curr_num
            if complement in counterparts.keys():
                return nums.index(complement), i
            counterparts[curr_num] = complement
        return [-1]

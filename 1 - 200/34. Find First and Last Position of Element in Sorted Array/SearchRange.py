"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        T(n) = O(logn) -- binary search to find starting index of target for twice
        S(n) = O(1) -- const time
        """
        if not nums:
            return [-1, -1]
        l = self.find(nums, target, True)
        if l >= len(nums) or nums[l] != target:
            return [-1, -1]
        return [l, self.find(nums, target, False)-1]
    
    def find(self, nums, target, is_left):
        l = 0
        r = len(nums)
        while l < r:
            i = (l+r)//2
            if nums[i] > target or (is_left and target == nums[i]):
                r = i
            else:
                l = i+1
        return l
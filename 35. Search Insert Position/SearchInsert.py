"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        T(n) = O(log n) -- binary search
        S(n) = O(1) -- const space
        """
        if not nums:
            return 0
        l = 0
        r = len(nums)-1
        
        if target < nums[l]:
            return l
        if target > nums[r]:
            return r + 1

        while l < r:
            mid = l+(r-l+1)//2
            if nums[mid-1] < target <= nums[mid]:
                return mid
            if nums[mid] < target:
                l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid
        return r
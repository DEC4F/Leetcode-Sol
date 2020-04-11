"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

1. You must not modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n2).
4. There is only one duplicate number in the array, but it could be repeated more than once.
"""
from collections import Counter


class Solution:
    def findDuplicate_floyd(self, nums: List[int]) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast

    def findDuplicate_sort(self, nums: List[int]) -> int:
        """
        T(n) = O(nlogn)
        S(n) = O(1)
        """
        nums.sort()
        for i, n in enumerate(nums[:-1]):
            if n == nums[i + 1]:
                return n

    def findDuplicate_hash(self, nums: List[int]) -> int:
        """
        T(n) = O(n)
        S(n) = O(n) -- MLE memory limit exceeds
        """
        return max(Counter(nums).items(), key=lambda x: x[1])[0]

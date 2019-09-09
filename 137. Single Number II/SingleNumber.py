"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
"""

class Solution:
    def singleNumber_hash(self, nums: List[int]) -> int:
        """
        T(n) = O(n) -- time to create a hash set
        S(n) = O(n) -- used hash set to store all distinct numbers
        """
        return (sum(set(nums))*3 - sum(nums))//2

    def singleNumber_bitops(self, nums: List[int]) -> int:
        """
        T(n) = O(n) one pass
        S(n) = O(1) no extra space used

        truth table:
        -----------
            first appearance:
                once = n
                twice = 0
            second appearance:
                once = 0
                twice = n
            third appearance:
                once = 0
                twice = 0
        """
        once = twice = 0
        for n in nums:
            once = ~twice & (once^n)
            twice = ~once & (twice^n)
        return once
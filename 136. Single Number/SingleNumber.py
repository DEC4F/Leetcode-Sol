"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        T(n) = O(n) -- traversed entire list
        S(n) = O(1) -- only used one var
        """
        ans = 0
        for n in nums:
            ans ^= n
        return ans

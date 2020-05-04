"""
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.
"""


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        i = -1
        for j, n in enumerate(nums):
            if n == 1:
                if i == -1:
                    i = j
                else:
                    if j - i - 1 < k:
                        return False
                    else:
                        i = j
        return True

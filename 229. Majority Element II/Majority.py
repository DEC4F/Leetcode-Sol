"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.
"""
import collections


class Solution:
    def majorityElement_boyer_moore(self, nums: List[int]) -> List[int]:
        """
        T(n) = O(n)
        S(n) = O(1)
        ---------
        only keep two variable because a list cannot have more than 2 elements appearing more than n // 3 times
        """
        if not nums:
            return []
        c1 = c2 = 0
        n1 = n2 = None
        for n in nums:
            if n == n1:
                c1 += 1
            elif n == n2:
                c2 += 1
            elif c1 == 0:
                c1, n1 = 1, n
            elif c2 == 0:
                c2, n2 = 1, n
            else:
                c1 -= 1
                c2 -= 1
        return [n for n in (n1, n2) if nums.count(n) > len(nums) // 3]

    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        res = []
        for n, c in collections.Counter(nums).items():
            if c > len(nums) // 3:
                res.append(n)
        return res
"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        T(n) = O(n) -- each pos is visited exactly once
        S(n) = O(1)
        ----------
        greedily search the pos with largest jump within rechable positions
        """
        n = len(nums)
        if n <= 1:
            return 0
        count, cur, reachables = 1, 0, nums[0]
        while reachables < n - 1:
            cur, reachables = reachables, max(
                i + nums[i] for i in range(cur, reachables + 1))
            count += 1
        return count

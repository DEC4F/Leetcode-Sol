"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob_dp(self, nums: List[int]) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        if not nums:
            return 0

        loot = [-1]*len(nums)
        for i, plunder in enumerate(nums):
            if i == 0:
                loot[i] = plunder
            elif i == 1:
                loot[i] = max(plunder, loot[0])
            else:
                loot[i] = max(loot[i-2]+plunder, loot[i-1])
        return loot[-1]

    def rob_dp_const(self, nums: List[int]) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        if not nums:
            return 0
        prev = 0
        curr = 0
        for p in nums:
            temp = curr
            curr = max(prev + p, curr)
            prev = temp
        return curr
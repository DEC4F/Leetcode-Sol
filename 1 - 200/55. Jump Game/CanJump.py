"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""


class Solution:

    def canJump_dp(self, nums: List[int]) -> bool:
        """
        T(n) = O(n^2) -- two passes in worst case
        S(n) = O(n) -- keepping a reachability state array
        """
        n = len(nums)
        # 0 for unknown, -1 for cannot reach goal, 1 for reachable
        state_arr = [0] * n
        state_arr[-1] = 1
        for i in reversed(
                range(n - 1)):  # start backwards from the last element
            max_jump = min(i + nums[i], n - 1)
            for j in range(i + 1, max_jump + 1):
                if state_arr[j] == 1:  # if there's a reachable pos from current position
                    state_arr[i] = 1  # then this is also a reachable pos
                    break
        return state_arr[0] == 1

    def canJump_greedy(self, nums: List[int]) -> bool:
        """
        T(n) = O(n) -- only one pass
        S(n) = O(1) -- no extra var
        """
        i = left_ptr = len(nums) - 1
        while i >= 0:
            if i + nums[i] >= left_ptr:
                left_ptr = i
            i -= 1
        return left_ptr == 0

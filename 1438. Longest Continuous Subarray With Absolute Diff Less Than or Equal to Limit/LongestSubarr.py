"""
Given an array of integers nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.

In case there is no subarray satisfying the given condition return 0.
"""
import bisect, collections


class Solution:
    def longestSubarray_asd_arr(self, nums: List[int], limit: int) -> int:
        """
        T(n) = O(n^2) -- pop oldest element could take n times in a for loop
        S(n) = O(n)
        """
        # L is sorted asd arr of valid window (max diff <= limit)
        i, L = 0, []
        for j, cur_num in enumerate(nums):
            bisect.insort(L, cur_num)
            if L[-1] - L[0] > limit:
                # remove oldest num
                L.pop(bisect.bisect_left(L, nums[i]))
                i += 1
        return j - i + 1

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        T(n) = O(n)
        S(n) = O(n) -- two dq used
        """
        max_dq = collections.deque() # dsd sorted
        min_dq = collections.deque() # asd sorted
        i = 0
        for n in nums:
            while max_dq and n > max_dq[-1]:
                # pop smallest num till n is smallest
                max_dq.pop()
            while min_dq and n < min_dq[-1]:
                # pop greatest num till n is greatest
                min_dq.pop()
            max_dq.append(n)
            min_dq.append(n)
            if max_dq[0] - min_dq[0] > limit:
                # pop oldest num in max and/or min dq
                if max_dq[0] == nums[i]:
                    max_dq.popleft()
                if min_dq[0] == nums[i]:
                    min_dq.popleft()
                # increment oldest num idx
                i += 1
        return len(nums) - i
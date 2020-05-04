"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = cnt = 0
        mp = {0: 0}
        for i, n in enumerate(nums, 1):
            if n:
                cnt += 1
            else:
                cnt -= 1
            if cnt in mp:
                res = max(res, i - mp[cnt])
            else:
                mp[cnt] = i
        return res

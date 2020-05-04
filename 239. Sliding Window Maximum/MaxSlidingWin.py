"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?
"""


class Solution:
    def maxSlidingWindow_hammer(self, nums: List[int], k: int) -> List[int]:
        """
        T(n) = O(NK)
        S(n) = O(K)
        """
        n = len(nums)
        if n * k == 0:
            return []
        return [max(nums[i: i + k]) for i in range(n - k + 1)]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        T(n) = O(N)
        S(n) = O(N)
        """
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        idx_dq = collections.deque()
        max_idx = 0

        # 0 ... k
        for i in range(k):
            if idx_dq and idx_dq[0] == i - k:
                idx_dq.popleft()
            while idx_dq and nums[i] > nums[idx_dq[-1]]:
                idx_dq.pop()
            idx_dq.append(i)
            if nums[i] > nums[max_idx]:
                max_idx = i

        # k ... n
        res = [nums[max_idx]]
        for i in range(k, n):
            if idx_dq and idx_dq[0] == i - k:
                idx_dq.popleft()
            while idx_dq and nums[i] > nums[idx_dq[-1]]:
                idx_dq.pop()
            idx_dq.append(i)
            res.append(nums[idx_dq[0]])
        return res

"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
"""

class Solution:
    def maxSlidingWindow_hammer(self, nums: List[int], k: int) -> List[int]:
        """
        T(n) = n*k = O(nk) -- hammer checks max of all arrays of length k
        S(n) = O(1) -- no extra variable
        """
        if not nums or not k:
            return []
        return [max(nums[i: i+k]) for i in range(len(nums) - k + 1)]

    def

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        T(n) = 2n = O(n) -- two pass
        S(n) = 2n = O(n) -- size of left and right array
        """
        if not nums or not k:
            return []
        n = len(nums)
        if k == 1:
            return nums

        left = [0]*n
        left[0] = nums[0]
        right = [0]*n
        right[n-1] = nums[n-1]

        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])
            j = n - i - 1
            if (j+1)%k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])

        ans = []
        for i in range(n - k + 1):
            ans.append(max(left[i+k-1], right[i]))
        return ans

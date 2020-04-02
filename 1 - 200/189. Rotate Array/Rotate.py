"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""


class Solution:
    def rotate_by_double_reverse(self, nums: List[int], k: int) -> None:
        """
        T(n) = n/2 + k/2 + (n-k)/2 = O(n)
        S(n) = O(1) -- in place swapping
        """
        if len(nums) <= k:  # const
            k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)  # n/2
        self.reverse(nums, 0, k - 1)  # (k-1)/2
        self.reverse(nums, k, len(nums) - 1)  # (n-k)/2

    def reverse(self, nums: List[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate_BF(self, nums: List[int], k: int) -> None:
        """
        T(n) = n*k = O(nk) -- insert takes O(n) time, repeated k times
        S(n) = O(1) -- will be using O(n) in other language
        """
        if len(nums) <= k:  # const
            k = k % len(nums)
        for _ in range(k):  # k
            nums.insert(0, nums.pop())  # n

    def rotate_extra_arr(self, nums: List[int], k: int) -> None:
        """
        T(n) = n + n = O(n)
        S(n) = O(n) -- used extra array
        """
        n = len(nums)
        if n <= k:  # const
            k = k % n
        ans = [-1] * n
        for i in range(n):  # n
            if i + k >= n:
                ans[(i + k) % n] = nums[i]
            else:
                ans[i + k] = nums[i]
        for i in range(n):  # n
            nums[i] = ans[i]

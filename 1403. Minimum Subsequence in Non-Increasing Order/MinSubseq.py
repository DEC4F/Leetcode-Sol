"""
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence.

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.

Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.
"""


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        """
        T(n) = O(nlogn) = nlogn + 2n
        S(n) = O(1)
        """
        res = []
        tot_res = 0
        tot_num = sum(nums)  # O(n)
        nums.sort()  # O(nlogn)
        while nums and tot_res <= tot_num:  # O(n)
            tot_res += nums[-1]
            tot_num -= nums[-1]
            res.append(nums.pop())
        return res

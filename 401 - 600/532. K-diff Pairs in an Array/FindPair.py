"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        T(n) = O(n) -- one pass to check all possible complements
        S(n) = O(n)
        """
        if not nums or len(nums) < 1 or k < 0:
            return 0
        c = {}
        ans = 0
        for n in nums:
            if c.get(n):
                if k == 0 and c[n] == 1:
                    ans += 1
                c[n] += 1
            else:
                if c.get(n - k):
                    ans += 1
                if c.get(n + k):
                    ans += 1
                c[n] = 1

        return ans
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
"""


class Solution:
    def longestConsecutive_sort(self, nums: List[int]) -> int:
        """
        T(n) = nlogn + n = O(nlogn) -- sorting
        S(n) = O(1) -- const space
        """
        if not nums or len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1

        ans = 1
        cur = 1
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] - nums[i - 1] == 1:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 1
        ans = max(ans, cur)
        return ans

    def longestConsecutive_union_find(self, nums: List[int]) -> int:
        """
        T(n) = O(n^2*a(n)) -- one for loop * check hash keys * union
        S(n) = 3n = O(n) -- par array, size array, hash map
        """
        if not nums or len(nums) < 1:
            return 0
        if len(nums) == 1:
            return 1

        par = [i for i in range(len(nums))]
        size = [1] * len(nums)
        seen_dict = {}
        self.ans = 1

        def find(x: int) -> int:
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x: int, y: int) -> bool:
            xroot = find(x)
            yroot = find(y)
            if xroot == yroot:
                return False
            if size[xroot] > size[yroot]:
                par[yroot] = xroot
                size[xroot] += size[yroot]
                self.ans = max(self.ans, size[xroot])
            else:
                par[xroot] = yroot
                size[yroot] += size[xroot]
                self.ans = max(self.ans, size[yroot])
            return True

        for i, n in enumerate(nums):
            if n in seen_dict.keys():
                continue
            seen_dict[n] = i
            if n + 1 in seen_dict.keys():
                union(seen_dict[n + 1], i)
            if n - 1 in seen_dict.keys():
                union(seen_dict[n - 1], i)

        return self.ans

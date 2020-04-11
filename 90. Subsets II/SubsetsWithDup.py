"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        if not nums or len(nums) < 1:
            return ans
        nums.sort()

        def dfs(start: int, k: int, path: List[int]) -> None:
            if k == 0:
                ans.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1, k - 1, path)
                path.pop()

        for k in range(1, len(nums) + 1):
            dfs(0, k, [])
        return ans

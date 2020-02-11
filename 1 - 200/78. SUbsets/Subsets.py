"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 1:
            return [[]]
        ans = [[]]
        
        def dfs(start: int, k: int, path: List[int]) -> None:
            if k == 0:
                ans.append(path[:])
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, k - 1, path)
                path.pop()
                
        for k in range(1, len(nums) + 1):
            dfs(0, k, [])
        return ans

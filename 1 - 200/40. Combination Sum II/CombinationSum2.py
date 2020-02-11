"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        T(n) = nlogn + O(n^d) where d is the max depth dfs will search
        S(n) = O(n^d) where d is the max depth dfs will search
        """
        ans = []
        candidates.sort()
        
        def dfs(target: int, path: List[int], start: int) -> None:
            if target == 0:
                ans.append(path)
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(target - candidates[i], path + [candidates[i]], i + 1)
                
        dfs(target, [], 0)
        return ans
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
        
        def dfs(target: int, combination: List[int], idx):
            if not target:
                ans.append(combination)
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(target-candidates[i], combination+[candidates[i]], i+1)
                
        dfs(target, [], 0)
        return ans
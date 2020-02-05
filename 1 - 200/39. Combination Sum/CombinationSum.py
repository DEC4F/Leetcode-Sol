"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        T(n) = nlogn + O(n^d) where d is the max depth dfs will search
        S(n) = O(n^d) where d is the max depth dfs will search
        """
        ans = []
        candidates.sort()
        def dfs(target: int, combination: List[int], idx: int) -> None:
            if not target:
                ans.append(combination)
                return
            for i in range(idx, len(candidates)):
                if candidates[i] > target:
                    break
                dfs(target-candidates[i], combination+[candidates[i]], i)
        dfs(target, [], 0)
        return ans
"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        T(n) = O()
        S(n) = O()
        """
        if n < 1 or n < k:
            return [[]]
        res = []

        def dfs(start: int, path: List[int]) -> None:
            if len(path) == k:
                res.append(path[:])
            for i in range(start, n + 1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()

        dfs(1, [])
        return res
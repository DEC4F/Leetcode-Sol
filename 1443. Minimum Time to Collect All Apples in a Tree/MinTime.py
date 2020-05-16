class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        T(n) = O(n) -- visit each node exactly once
        S(n) = O(n)
        """
        def dfs(u):
            if u in visited:
                return 0
            visited.add(u)
            res = 0
            for v in mat[u]:
                res += dfs(v)
            if res > 0:
                return res + 2
            if hasApple[u]:
                return 2
            return 0
        mat = [[] for _ in range(n)]
        for u, v in edges:
            mat[u].append(v)
            mat[v].append(u)
        visited = set()
        return max(dfs(0) - 2, 0)
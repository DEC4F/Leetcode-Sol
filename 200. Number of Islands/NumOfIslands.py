"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class UnionFind:
    def __init__(self, n, cnt):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.res = cnt

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] > self.rank[y_root]:
            self.par[y_root] = x_root
        elif self.rank[y_root] > self.rank[x_root]:
            self.par[x_root] = y_root
        else:
            self.par[y_root] = x_root
            self.rank[x_root] += 1
        self.res -= 1


class Solution:
    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        """
        T(n) = O(m*n) -- traversed the entire grid
        T(n) = O(min(m,n)) -- might store up to m or n coord info if the entire grid is filled by land
        """
        if not grid:
            return 0
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    ans += 1
                    grid[r][c] = '0'
                    from collections import deque
                    dq = deque([(r, c), ])
                    while dq:
                        row, col = dq.popleft()
                        if row + 1 < len(grid) and grid[row + 1][col] == '1':
                            dq.append((row + 1, col))
                            grid[row + 1][col] = '0'
                        if row - 1 >= 0 and grid[row - 1][col] == '1':
                            dq.append((row - 1, col))
                            grid[row - 1][col] = '0'
                        if col + \
                                1 < len(grid[0]) and grid[row][col + 1] == '1':
                            dq.append((row, col + 1))
                            grid[row][col + 1] = '0'
                        if col - 1 >= 0 and grid[row][col - 1] == '1':
                            dq.append((row, col - 1))
                            grid[row][col - 1] = '0'
        return ans

    def numIslands_union_find(self, grid: List[List[str]]) -> int:
        """
        T(n) = O(n*m) -- finding all 1s
        S(n) = O(n*m) -- size of parent array
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        uf = UnionFind(
            n * m, sum(grid[i][j] == '1' for i in range(n) for j in range(m)))
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1':
                    if r + 1 < n and grid[r + 1][c] == '1':
                        uf.union(m * r + c, m * (r + 1) + c)
                    if c + 1 < m and grid[r][c + 1] == '1':
                        uf.union(m * r + c, m * r + c + 1)
        return uf.res

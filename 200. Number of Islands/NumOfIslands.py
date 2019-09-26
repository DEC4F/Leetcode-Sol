class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    ans += 1
                    grid = self.one_island_bfs(r, c, grid)
        return ans

    def one_island_bfs(self, r, c, grid):
        from collections import deque
        dq = deque([grid[r][c],])
        while dq:
            if grid[r+1][c] == '1':
                dq.append(grid[r+1][c])
            if grid[r-1][c] == '1':
                dq.append(grid[r-1][c])
            if grid[r][c+1] == '1':
                dq.append(grid[r][c+1])
            if grid[r][c-1] == '1':
                dq.append(grid[r][c-1])
            grid[r][c] = '0'
            dq.popleft()
        return grid

a = Solution()
print(a.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
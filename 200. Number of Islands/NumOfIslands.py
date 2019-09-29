"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
                    dq = deque([(r,c),])
                    while dq:
                        row, col = dq.popleft()
                        if row+1 < len(grid) and grid[row+1][col] == '1':
                            dq.append((row+1, col))
                            grid[row+1][col] = '0'
                        if row-1 >= 0 and grid[row-1][col] == '1':
                            dq.append((row-1, col))
                            grid[row-1][col] = '0'
                        if col+1 < len(grid[0]) and grid[row][col+1] == '1':
                            dq.append((row, col+1))
                            grid[row][col+1] = '0'
                        if col-1 >= 0 and grid[row][col-1] == '1':
                            dq.append((row, col-1))
                            grid[row][col-1] = '0'
        return ans
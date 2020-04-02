"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        T(n) = O(n) -- explored all cells
        S(n) = O(n) -- size of queue
        """
        if len(grid) < 1 or len(grid[0]) < 1:
            return 0
        R, C = len(grid), len(grid[0])
        queue = collections.deque()

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 2:
                    queue.append((r, c, 0))

        def neighbors(r, c):
            for new_r, new_c in (
                    (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= new_r < R and 0 <= new_c < C:
                    yield new_r, new_c

        res = 0
        while queue:
            r, c, res = queue.popleft()
            for new_r, new_c in neighbors(r, c):
                if grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    queue.append((new_r, new_c, res + 1))

        if any(1 in row for row in grid):
            return -1
        return res

"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

- Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
- C_1 is at location (0, 0) (ie. has value grid[0][0])
- C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
- If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        T(n) = O(n) -- explored all nodes in worst case
        S(n) = O(n) -- size of queue in worst case
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        queue = collections.deque()
        queue.append((0, 0, 1))

        def neighbors(i: int, j: int) -> (int, int):
            all_neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
            for new_i, new_j in all_neighbors:
                if 0 <= new_i < n and 0 <= new_j < n:
                    yield new_i, new_j

        while queue:
            cur_i, cur_j, dist = queue.popleft()
            if cur_i == n - 1 and cur_j == n - 1:
                return dist
            for new_i, new_j in neighbors(cur_i, cur_j):
                if grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = 1
                    queue.append((new_i, new_j, dist + 1))
        return -1
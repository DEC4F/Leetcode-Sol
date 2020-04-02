"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands2(self, m: int, n: int,
                    positions: List[List[int]]) -> List[int]:
        """
        T(n) = O(L) -- number of operations performed
        S(n) = O(m*n) -- size of union find array
        """
        if m * n == 0:
            return [0] * len(positions)

        self.par = [-1] * (m * n)
        self.rank = [0] * (m * n)
        self.count = 0

        ans = []
        for move in positions:
            i, j = move[0], move[1]
            neighbors = []

            if i - 1 >= 0 and self.is_valid((i - 1) * n + j):
                neighbors.append((i - 1) * n + j)
            if i + 1 < m and self.is_valid((i + 1) * n + j):
                neighbors.append((i + 1) * n + j)
            if j - 1 >= 0 and self.is_valid(i * n + j - 1):
                neighbors.append(i * n + j - 1)
            if j + 1 < n and self.is_valid(i * n + j + 1):
                neighbors.append(i * n + j + 1)

            idx = i * n + j
            self.set_par(idx)
            for neigh in neighbors:
                self.union(idx, neigh)
            ans.append(self.count)
        return ans

    def find(self, x: int) -> int:
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        if self.rank[xroot] > self.rank[yroot]:
            self.par[yroot] = xroot
        elif self.rank[yroot] > self.rank[xroot]:
            self.par[xroot] = yroot
        else:
            self.par[yroot] = xroot
            self.rank[xroot] += 1
        self.count -= 1
        return True

    def set_par(self, x: int) -> None:
        if self.par[x] == -1:
            self.par[x] = x
            self.count += 1

    def is_valid(self, x: int) -> bool:
        return self.par[x] >= 0

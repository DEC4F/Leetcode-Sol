"""
You are given a m x n 2D grid initialized with these three possible values.

1. -1 - A wall or an obstacle.
2.  0 - A gate.
3.  INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        T(n) = O(n) -- visited all nodes
        S(n) = O(n) -- size of queue
        """
        if len(rooms) < 1 or len(rooms[0]) < 1:
            return
        queue = collections.deque()
        for i, row in enumerate(rooms):
            for j, cell in enumerate(row):
                if cell == 0:
                    queue.append((i, j, 0))

        def generate_neighbors(i: int, j: int) -> (int, int):
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for new_i, new_j in neighbors:
                if 0 <= new_i < len(rooms) and 0 <= new_j < len(rooms[0]):
                    yield (new_i, new_j)

        while queue:
            i, j, dist = queue.popleft()
            for new_i, new_j in generate_neighbors(i, j):
                if rooms[new_i][new_j] > dist + 1:
                    rooms[new_i][new_j] = dist + 1
                    queue.append((new_i, new_j, dist + 1))

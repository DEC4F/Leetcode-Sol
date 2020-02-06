"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        T(n) = O(MN) -- traversed all cells in the M*N board
        S(n) = O(1)
        """
        if len(board) < 1 or len(board[0]) < 1:
            return
        
        def neighbors(i: int, j: int) -> (int, int):
            all_neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
            for new_i, new_j in all_neighbors:
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                    yield new_i, new_j
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                n_live_neighbor = 0
                for new_i, new_j in neighbors(i, j):
                    if abs(board[new_i][new_j]) == 1:
                        n_live_neighbor += 1
                if cell == 1:
                    # rule 2: stay the same
                    if 2 <= n_live_neighbor <= 3:
                        continue
                    # rule 1 and 3: death by under/over population
                    else:
                        board[i][j] = -1
                else:
                    # rule 4: reproduction
                    if n_live_neighbor == 3:
                        board[i][j] = 2
        
        # change "marked" cell to actual state
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == -1:
                    board[i][j] = 0
                elif cell == 2:
                    board[i][j] = 1
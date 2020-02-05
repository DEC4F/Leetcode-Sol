"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        T(n) = O(m*n*4^l) -- size of the board and each cell can go 4 directions
        S(n) = O(L) -- size of stack grows to size of the word at most
        """
        if len(word) < 1 or len(board) < 1 or len(board[0]) < 1:
            return False
        def rec(x: int, y: int, cur_len: int) -> bool:
            if cur_len == len(word):
                return True
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return False
            if board[x][y] != word[cur_len]:
                return False
            temp = board[x][y]
            board[x][y] = None
            res = rec(x - 1, y, cur_len + 1) or rec(x + 1, y, cur_len + 1) or rec(x, y - 1, cur_len + 1) or rec(x, y + 1, cur_len + 1)
            board[x][y] = temp
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if rec(i, j, 0):
                    return True
        return False

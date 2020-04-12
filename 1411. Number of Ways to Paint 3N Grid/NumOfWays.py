"""
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.
"""


class Solution:
    def numOfWays(self, n: int) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        ---------
        for first row, we have two patterns:
            aba: 121, 131, 212, 232, 313, 323
            abc: 123, 132, 213, 231, 312, 321
        for the next row, the two pattern can be followed by:
            aba_2: 212, 232, 313, 213, 312 (assuming aba_1 = 121)
            abc_2: 212, 232, 231, 312 (assuming abc_1 = 123)
        aba_2 can be 2 abc or 3 abc
        abc_2 can be 2 aba or 2 abc
        so the state func:
            [aba_i, abc_i] = [[3, 2], [2, 2]] * [aba_i-1, abc_i-1]
        """
        abc, aba = 6, 6
        for _ in range(1, n):
            abc, aba = abc * 2 + aba * 2, abc * 2 + aba * 3
        return (abc + aba) % (10 ** 9 + 7)
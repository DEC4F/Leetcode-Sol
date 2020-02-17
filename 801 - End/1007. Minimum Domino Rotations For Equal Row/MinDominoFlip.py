"""
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
"""
class Solution:
    def minDominoRotations_greedy(self, A: List[int], B: List[int]) -> int:
        """
        T(n) = O(n) -- iterate thru all As and Bs
        S(n) = O(1) -- const space
        """
        n = len(A)
        res = float('inf')
        for val in [A[0], B[0]]:
            a_count, b_count = 0, 0
            for i in range(n):
                if A[i] != val and B[i] != val:
                    a_count, b_count = float('inf'), float('inf')
                    break
                elif A[i] != val:
                    a_count += 1
                elif B[i] != val:
                    b_count += 1
            res = min(res, a_count, b_count)
        if res == float('inf'):
            return -1
        return res
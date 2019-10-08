"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        T(n) = O(mn) -- traversed both words
        S(n) = O(mn) -- used 2d array to store sol of each subprob
        """
        m = len(word1)
        n = len(word2)
        if m*n == 0:
            return m+n
        dist = [[-1]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dist[i][0] = i
        for j in range(1, n+1):
            dist[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dist[i][j] = 1 + min(dist[i-1][j], dist[i][j-1], dist[i-1][j-1]-1)
                else:
                    dist[i][j] = 1 + min(dist[i-1][j], dist[i][j-1], dist[i-1][j-1])
        return dist[m][n]
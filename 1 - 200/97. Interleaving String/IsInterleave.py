"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
"""

class Solution:
    def isInterleave_2d_dp(self, s1: str, s2: str, s3: str) -> bool:
        """
        T(n) = n*m = O(nm) -- nested loops to assign value to boolean matrix
        S(n) = n+m = O(nm) -- state trans matrix
        """
        n = len(s1)
        m = len(s2)
        if n+m != len(s3):
            return False

        mat = [[False]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if not (i or j):
                    mat[0][0] = True
                elif not i:
                    mat[0][j] = mat[0][j-1] and (s2[j-1] == s3[j-1])
                elif not j:
                    mat[i][0] = mat[i-1][0] and (s1[i-1] == s3[i-1])
                else:
                    up = mat[i-1][j]
                    left = mat[i][j-1]
                    if (up and s1[i-1] == s3[i+j-1]) or (left and s2[j-1] == s3[i+j-1]):
                        mat[i][j] = True
        return mat[n][m]
    
    def isInterleave_1d_dp(self, s1: str, s2: str, s3: str) -> bool:
        """
        T(n) = n*m = O(nm) -- nested loops to assign value to boolean matrix
        S(n) = m = O(m) -- state trans array
        """
        n = len(s1)
        m = len(s2)
        if n+m != len(s3):
            return False

        states = [False]*(m+1)
        for i in range(n+1):
            for j in range(m+1):
                if not (i or j):
                    states[0] = True
                elif not i:
                    states[j] = states[j-1] and (s2[j-1] == s3[j-1])
                elif not j:
                    states[0] = states[0] and (s1[i-1] == s3[i-1])
                else:
                    states[j] = (states[j] and s1[i-1] == s3[i+j-1]) or (states[j-1] and s2[j-1] == s3[i+j-1])
        return states[m]
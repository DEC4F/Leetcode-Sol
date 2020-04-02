"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.
"""


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        """
        T(n) = O(n^2) -- traverse all cells in adj matrix, that's two nested loops over N friends
        S(n) = O(n) -- size of union find
        """
        if not M or len(M) < 1 or len(M[0]) < 1:
            return 0
        N = len(M)
        par = [i for i in range(N)]
        rank = [0] * N

        def find(x: int) -> int:
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]

        def union(x: int, y: int) -> bool:
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return False
            if rank[xroot] > rank[yroot]:
                par[yroot] = xroot
            elif rank[xroot] < rank[yroot]:
                par[xroot] = yroot
            else:
                par[yroot] = xroot
                rank[xroot] += 1
            return True

        # only search half of the matrix
        for r in range(N):
            for c in range(r):
                if M[r][c] == 1 and r != c:
                    union(r, c)
        res = 0
        for i, p in enumerate(par):
            if i == p:
                res += 1
        return res

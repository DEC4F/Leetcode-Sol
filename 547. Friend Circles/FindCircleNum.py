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
        self.par = [i for i in range(N)]
        self.rank = [0]*N
        ans = 0

        for i in range(N):
            for j in range(N):
                if M[i][j] == 1 and i != j:
                    self.union(i, j)
        for i, par in enumerate(self.par):
            if i == par:
                ans += 1
        return ans

    def find(self, x: int) -> int:
        if self.par[x] != x:
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
        return True

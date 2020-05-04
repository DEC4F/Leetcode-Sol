"""
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
"""
from collections import defaultdict


class Solution:
    def smallestStringWithSwaps_union_find(
            self, s: str, pairs: List[List[int]]) -> str:
        """
        T(n) = logn + 2n + nlogn =  O(nlogn)
        S(n) = O(n)
        """
        n = len(s)
        if n < 1:
            return s

        uf = UnionFind(n)
        mp = defaultdict(list)
        res = ''

        for i, j in pairs:
            uf.union(i, j)
        for i in range(n):
            mp[uf.find(i)].append(s[i])
        for k in mp.keys():
            mp[k].sort(reverse=True)
        for i in range(n):
            res += mp[uf.find(i)].pop()
        return res

    def smallestStringWithSwaps_dfs(
            self, s: str, pairs: List[List[int]]) -> str:
        if len(pairs) < 1:
            return s

        def dfs(node: str, seen: List[str]):
            if node in seen:
                return
            seen.append(node)
            self.res = min(self.res, node)
            for i, j in pairs:
                new_node = self.swap(node, i, j)
                dfs(new_node, seen)

        self.res = s
        dfs(s, [])
        return self.res

    def swap(self, s, i, j):
        s = list(s)
        s[i], s[j] = s[j], s[i]
        return ''.join(s)


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] > self.rank[y_root]:
            self.par[y_root] = x_root
        elif self.rank[x_root] < self.rank[y_root]:
            self.par[x_root] = y_root
        else:
            self.par[y_root] = x_root
            self.rank[x_root] += 1
        return True

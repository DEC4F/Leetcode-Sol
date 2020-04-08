"""
Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from the vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices it jumps randomly to one of them with the same probability, otherwise, when the frog can not jump to any unvisited vertex it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting directly the vertices fromi and toi.

Return the probability that after t seconds the frog is on the vertex target.
"""


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        """
        T(n) = O(n) -- visit each node exactly once
        S(n) = O(n^2) -- adjacency list
        """
        if n == 1:
            return 1.0
        visited = [False] * (n + 1)
        G = [[] for _ in range(n + 1)]
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)

        def dfs(node, t_left):
            if visited[node]:
                return 0
            if t_left == 0 or node != 1 and len(G[node]) == 1:
                return node == target
            visited[node] = True
            res = 1 / (len(G[node]) - (node != 1)) # node 1 has no parent node
            return res * max(dfs(child, t_left - 1) for child in G[node])

        return dfs(1, t)
"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        T(n) = O(n^2) -- traversed all edges, which is n^2 in complete graph
        S(n) = O(n) -- size of parent array
        """
        if len(edges) == 0: return n == 1

        par = [i for i in range(n)]
        count = n

        def find(x: int) -> int:
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]
        
        def union(x: int, y: int) -> bool:
            xroot = find(x)
            yroot = find(y)
            if xroot == yroot: return False
            par[yroot] = xroot
            return True
        
        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return False
            else:
                union(edge[0], edge[1])
                count -= 1
        return count == 1
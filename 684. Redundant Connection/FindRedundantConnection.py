"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        T(n) = O(n^2) -- traversed all edges, which is n^2 in worst case
        S(n) = O(n) -- size of parent array
        """
        if len(edges) == 0: return []
        par = [i for i in range(len(edges)+1)]
        
        def find(x: int) -> int:
            if x == par[x]:
                return x
            return find(par[x])
        
        def union(x: int, y: int) -> bool:
            xroot, yroot = find(x), find(y)
            if xroot == yroot: return False
            par[xroot] = yroot
            return True

        for edge in edges:
            if find(edge[0]) == find(edge[1]): 
                return edge
            union(edge[0], edge[1])
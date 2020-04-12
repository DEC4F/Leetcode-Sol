"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.
"""


class Solution:
    def criticalConnections(
            self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        T(n) = O(|V| + |E|) -- find_adj_list costs O(|E|) and find_scc costs O(|V|) by visiting every unvisited node in one run
        S(n) = O(|V|)
        """
        res = []
        visited = [False] * n
        scc_ids = [i for i in range(n)]
        adj_list = self.find_adj_list(n, connections)
        self.find_scc(res, adj_list, scc_ids, visited, 0, -1, 0)
        return res

    def find_scc(self,
                 res: List[int],
                 adj_list: List[List[int]],
                 scc_ids: List[int],
                 visited: List[bool],
                 rank: int,
                 prev: int,
                 u: int) -> None:
        """
        T(n) = O(|V|) -- visiting all unvisited neighbors, at most |V|
        """
        visited[u] = True
        scc_ids[u] = rank

        for v in adj_list[u]:
            if prev == v:
                continue
            # recurse if hasn't visited this neighbor yet
            if not visited[v]:
                self.find_scc(
                    res,
                    adj_list,
                    scc_ids,
                    visited,
                    rank + 1,
                    u,
                    v)
            # update the scc_ids to group components of SCC
            scc_ids[u] = min(scc_ids[v], scc_ids[u])

            # if scc_ids of the neighbor >= the initially assigned value
            # then its a cross edge
            # because two neighboring SCC would differ by at least 1 in SCC id.
            if scc_ids[v] >= rank + 1:
                res.append([u, v])

    def find_adj_list(self, n: int,
                      connections: List[List[int]]) -> List[List[int]]:
        """
        T(n) = O(|E|) -- looping through all edges to construct adjacency list
        """
        adj_list = [[] for _ in range(n)]
        for u, v in connections:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list

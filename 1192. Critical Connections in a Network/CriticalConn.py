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
                 cur_rank: int,
                 prev_node: int,
                 cur_node: int) -> None:
        """
        T(n) = O(|V|) -- visiting all unvisited neighbors, at most |V|
        """
        visited[cur_node] = True
        scc_ids[cur_node] = cur_rank

        for next_node in adj_list[cur_node]:
            if prev_node == next_node:
                continue
            # recurse if hasn't visited this neighbor yet
            if not visited[next_node]:
                self.find_scc(
                    res,
                    adj_list,
                    scc_ids,
                    visited,
                    cur_rank + 1,
                    cur_node,
                    next_node)
            # update the scc_ids to group components of SCC
            scc_ids[cur_node] = min(scc_ids[cur_node], scc_ids[next_node])

            # if scc_ids of the neighbor >= the initially assigned value
            # then its a cross edge
            # because two neighboring SCC would differ by at least 1 in SCC id.
            if scc_ids[next_node] >= cur_rank + 1:
                res.append([cur_node, next_node])

    def find_adj_list(self, n: int,
                      connections: List[List[int]]) -> List[List[int]]:
        """
        T(n) = O(|E|) -- looping through all edges to construct adjacency list
        """
        adj_list = [[] for _ in range(n)]
        for conn in connections:
            adj_list[conn[0]].append(conn[1])
            adj_list[conn[1]].append(conn[0])
        return adj_list

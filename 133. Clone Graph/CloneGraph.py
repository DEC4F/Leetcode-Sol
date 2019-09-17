"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph_BFS(self, node: 'Node') -> 'Node':
        """
        T(n) = O(n) -- traversed all nodes
        S(n) = O(n) -- used a queue and a dict, taking up 2N spaces
        """
        if not (node and node.val and node.neighbors):
            return Node(node.val, node.neighbors)

        from collections import deque
        dq = deque([node,])
        copy = Node(node.val, [])
        copy_dict = {node:copy}

        while dq:
            curr_node = dq.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in copy_dict: # if current neighbor is unvisited
                    neighbor_copy = Node(neighbor.val, [])
                    copy_dict[neighbor] = neighbor_copy # we store the original:copy pair in the dict
                    copy_dict[curr_node].neighbors.append(neighbor_copy) # we add the copy to the neighbor list of copied current node
                    dq.append(neighbor) # add neighbor to dq to expand
                else:
                    copy_dict[curr_node].neighbors.append(copy_dict[neighbor]) # if visited, add copied neighbor to current copied node's neighbor list
        return copy

    def cloneGraph_DFS(self, node: 'Node') -> 'Node':
        """
        T(n) = O(n) -- traversed all nodes
        S(n) = O(n) -- recursion stack at most N spaces
        """
        if not(node and node.val and node.neighbors):
            return Node(node.val, node.neighbors)
        def clone(node: 'Node', seen: {'Node':'Node'}) -> 'Node':
            for neighbor in node.neighbors:
                if neighbor in seen:
                    seen[node].neighbors.append(seen[neighbor])
                else:
                    neighbor_copy = Node(neighbor.val, [])
                    seen[neighbor] = neighbor_copy
                    seen[node].neighbors.append(neighbor_copy)
                    clone(neighbor, seen)
        node_copied = Node(node.val, [])
        seen = {node : node_copied}
        clone(node, seen)
        return node_copied

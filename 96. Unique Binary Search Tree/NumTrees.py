"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""
class Solution:
    def numTrees(self, n: int) -> int:
        """
        num unique tree = (num left subtree of root i * num right sub tree of root i) for i = 1 to n
        T(n) = O(n^2)
        S(n) = O(n)
        """
        G = [0]*(n+1)
        G[0] = 1
        G[1] = 1
        for root in range(2, n+1):
            for l in range(1, root+1):
                G[root] += G[l-1]*G[root-l]
        return G[n]

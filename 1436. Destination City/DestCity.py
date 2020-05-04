"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
"""


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        a = set()
        b = set()
        for c1, c2 in paths:
            a.add(c1)
            b.add(c2)
        return (b - a).pop()
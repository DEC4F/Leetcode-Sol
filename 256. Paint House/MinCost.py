"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
"""


class Solution:
    def minCost_recursion_memo(self, costs: List[List[int]]) -> int:
        """
        T(n) = O(n) = 3*n -- at most 3 possible branches at each node, n nodes
        S(n) = O(n) -- size of stack
        """
        ans = 0
        if not costs or len(costs) < 1 or len(costs[0]) != 3:
            return ans
        memo = {}

        def paint(n: int, color: int) -> int:
            if (n, color) in memo:
                return memo[(n, color)]
            total_cost = costs[n][color]
            # return leaf node
            if n == len(costs) - 1:
                pass
            # checking branches, ignore same color branch
            elif color == 0:
                total_cost += min(paint(n + 1, 1), paint(n + 1, 2))
            elif color == 1:
                total_cost += min(paint(n + 1, 0), paint(n + 1, 2))
            else:
                total_cost += min(paint(n + 1, 0), paint(n + 1, 1))
            # memo the result so other branch don't need to re-compute
            memo[(n, color)] = total_cost
            return total_cost
        return min(paint(0, 0), paint(0, 1), paint(0, 2))

    def minCost_DP_bottom_up(self, costs: List[List[int]]) -> int:
        """
        T(n) = O(n) -- visited n nodes, min takes O(1)
        S(n) = O(1) -- in place
        """
        if not costs or len(costs) < 1 or len(costs[0]) != 3:
            return 0
        n = len(costs)
        for i in range(n - 2, -1, -1):
            costs[i][0] += min(costs[i + 1][1], costs[i + 1][2])
            costs[i][1] += min(costs[i + 1][0], costs[i + 1][2])
            costs[i][2] += min(costs[i + 1][0], costs[i + 1][1])
        return min(costs[0])

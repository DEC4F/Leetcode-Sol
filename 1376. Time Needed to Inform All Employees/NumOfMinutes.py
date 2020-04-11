"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company has is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also it's guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the employees of the company of an urgent piece of news. He will inform his direct subordinates and they will inform their subordinates and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.
"""
from collections import defaultdict


class Solution:
    def numOfMinutes_two_pass(self, n: int,
                              headID: int,
                              manager: List[int],
                              informTime: List[int]) -> int:
        """
        T(n) = O(n) = 2n -- one loop to build dict and one to calc time
        S(n) = O(n) = 2n -- size of stack and dict
        """
        sub = defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                sub[m].append(i)

        def dfs(emp):
            if sub.get(emp) is None:
                return informTime[emp]
            return informTime[emp] + max(dfs(s) for s in sub[emp])

        return dfs(headID)

    def numOfMinutes_one_pass(self, n: int,
                              headID: int,
                              manager: List[int],
                              informTime: List[int]) -> int:
        """
        T(n) = O(n) -- one loop to calc time
        S(n) = O(n) -- size of stack only
        """
        def dfs(emp):
            if manager[emp] != -1:
                informTime[emp] += dfs(manager[emp])
                manager[emp] = -1
            return informTime[emp]

        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        return res

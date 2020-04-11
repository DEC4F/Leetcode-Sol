"""
There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.
"""
from heapq import heappush, heappop


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """
        T(n) = O(nlogn + nlogk) sort + pq
        S(n) = O(n)
        """
        team = []
        res = tot_s = 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heappush(team, s)
            tot_s += s
            if len(team) > k:
                tot_s -= heappop(team)
            res = max(res, tot_s * e)
        return res % (10 ** 9 + 7)
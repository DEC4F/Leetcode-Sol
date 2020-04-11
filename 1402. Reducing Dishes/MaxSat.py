"""
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  time[i]*satisfaction[i]

Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
"""


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        T(n) = O(nlogn) = nlogn + n
        S(n) = O(1)
        ----------
        res += tot will keep rollingly inc the time weight on the best dish
        e.g:
            res = tot = 0
            tot += a -> a
            res += tot -> a
            tot += b -> a + b
            res += tot -> 2a + b
            tot += c -> a + b + c
            res += tot -> 3a + 2b + c
            ...
        will stop if it starts to hurt overall res (last in stack + tot is negative)
        """
        res = tot = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] + tot > 0:
            tot += satisfaction.pop()
            res += tot
        return res

"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        """
        T(n) = O(n) -- greedy, one pass
        S(n) = O(1) -- no extra space
        """
        if intervals is None or (not any(intervals)):
            return [newInterval]
        if newInterval is None or len(newInterval) == 0:
            return intervals
        new_start, new_end = newInterval
        i = 0
        n = len(intervals)
        ans = []
        while i < n and intervals[i][0] < new_start:
            ans.append(intervals[i])
            i += 1
        if len(ans) == 0 or ans[-1][1] < new_start:
            ans.append(newInterval)
        else:
            ans[-1][1] = max(ans[-1][1], new_end)
        while i < n:
            curr_start, curr_end = intervals[i]
            if ans[-1][1] < curr_start:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], curr_end)
            i += 1
        return ans

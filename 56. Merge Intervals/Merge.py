"""
Given a collection of intervals, merge all overlapping intervals.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        T(n) = O(nlogn) -- sorting takes nlogn time and it traverses the list one time
        S(n) = O(1) -- const space
        """
        if intervals is None or len(intervals) == 0 or (not any(intervals)):
            return []
        intervals.sort(key=lambda x: x[0])
        ans = []
        for lst in intervals:
            if len(ans) != 0 and ans[-1][1] >= lst[0]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], lst[1])]
            else:
                ans.append(lst)
        return ans
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        T(n) = n + nlogn = O(nlogn) -- sort and one pass
        S(n) = O(1)
        """
        if len(intervals) < 1 or len(intervals[0]) < 1:
            return True
        intervals.sort(key=lambda m : m[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
"""
from heapq import heappush, heappop


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        T(n) = O(nlogn) -- sort and heap sort takes 2nlogn time
        S(n) = O(n) -- size of heap
        """
        if len(intervals) < 1:
            return 0
        room_heap = []  # heap that records the end time
        intervals.sort(key=lambda m: m[0])
        heappush(room_heap, intervals[0][1])

        for i in range(1, len(intervals)):
            # if endtime of most available room is earlier than start time of
            # cur meeting
            if room_heap[0] <= intervals[i][0]:
                heappop(room_heap)
            heappush(room_heap, intervals[i][1])
        return len(room_heap)

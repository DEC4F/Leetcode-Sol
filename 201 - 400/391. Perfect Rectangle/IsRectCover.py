"""
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
"""
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        T(n) = O(n) -- one pass
        S(n) = O(n) -- size of set
        ----------
        each corner will appear exactly 2 or 4 times, except for the corner of the big rectangle formed, so the remaining element should be a b c d
        if overlapping, the area wouldn't match
        """
        a, b, c, d, area = float('inf'), float('inf'), float('-inf'), float('-inf'), 0
        corners = set()
        for (x1, y1, x2, y2) in rectangles:
            a, b, c, d = min(x1, a), min(y1, b), max(x2, c), max(y2, d)
            area += (x2 - x1) * (y2 - y1)
            corners ^= {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}
        return corners == {(a, b), (c, d), (a, d), (c, b)} and area == (c - a) * (d - b)

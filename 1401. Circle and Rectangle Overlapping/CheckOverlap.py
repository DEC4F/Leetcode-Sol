"""
Given a circle represented as (radius, x_center, y_center) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return True if the circle and rectangle are overlapped otherwise return False.

In other words, check if there are any point (xi, yi) such that belongs to the circle and the rectangle at the same time.
"""
from math import sqrt


class Solution:
    def checkOverlap(
            self,
            radius: int,
            x_center: int,
            y_center: int,
            x1: int,
            y1: int,
            x2: int,
            y2: int) -> bool:
        """
        T(n) = O(1)
        S(n) = O(1)
        """
        # Case 1: center is inside of rect
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True

        # Case 2: center is outside but x or y coord is inside [x1, x2] or [y1,
        # y2]
        d1 = self.dist_to_edge(x1, x_center)
        d2 = self.dist_to_edge(x2, x_center)
        d3 = self.dist_to_edge(y1, y_center)
        d4 = self.dist_to_edge(y2, y_center)
        if x1 <= x_center <= x2:
            return radius >= d3 or radius >= d4
        if y1 <= y_center <= y2:
            return radius >= d1 or radius >= d2

        # Case 3: center is outside and coord is also outside both rect ranges
        d2c1 = self.dist_to_corner((x_center, y_center), (x1, y1))
        d2c2 = self.dist_to_corner((x_center, y_center), (x1, y2))
        d2c3 = self.dist_to_corner((x_center, y_center), (x2, y1))
        d2c4 = self.dist_to_corner((x_center, y_center), (x2, y2))
        return any(radius > d2c for d2c in [d2c1, d2c2, d2c3, d2c4])

    def dist_to_edge(self, x1, x2):
        return abs(x1 - x2)

    def dist_to_corner(self, p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

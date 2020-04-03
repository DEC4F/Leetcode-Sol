"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
"""


class Solution:
    def largestRectangleArea_BF(self, heights: List[int]) -> int:
        """
        T(n) = O(n^2) -- TLE
        S(n) = O(1)
        """
        if not heights:
            return 0
        res = 0
        n = len(heights)
        for i in range(n):
            min_h = float('inf')
            for j in range(i, n):
                min_h = min(min_h, heights[j])
                max_w = j - i + 1
                res = max(res, min_h * max_w)
        return res

    def largestRectangleArea_DC(self, heights: List[int]) -> int:
        """
        T(n) = O(n^2) -- TLE, n^2 in sorted array
        S(n) = O(n)
        """
        if not heights:
            return 0

        def rec(l: int, r: int) -> int:
            if l > r:
                return 0
            min_idx = l
            # finding min idx
            for i in range(l, r + 1):
                if heights[min_idx] > heights[i]:
                    min_idx = i

            # divide
            left_area = rec(l, min_idx - 1)
            right_area = rec(min_idx + 1, r)

            # conquer
            cur_area = heights[min_idx] * (r - l + 1)

            # combine
            return max(cur_area, left_area, right_area)

        return rec(0, len(heights) - 1)

    def largestRectangleArea_stack(self, heights: List[int]) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        ---------
        max_area_w_current_height = cur_height * (right_border_idx - left_border_index - 1)
        where r_idx is the next index to be pushed into the stack, l_idx is the previous index in the stack
        """
        if not heights:
            return 0
        stack = [-1]
        res = 0
        # build a monotone inc stack
        for i, h in enumerate(heights):
            # check out the max area when popping an ele
            while stack[-1] != -1 and h <= heights[stack[-1]]:
                area = heights[stack.pop()] * (i - stack[-1] - 1)
                res = max(res, area)
            stack.append(i)
        # check out the max area of all remaining ele
        while stack[-1] != -1:
            area = heights[stack.pop()] * (len(heights) - stack[-1] - 1)
            res = max(res, area)
        return res

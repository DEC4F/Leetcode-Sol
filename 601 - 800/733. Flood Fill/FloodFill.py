"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
"""


class Solution:
    def floodFill_BFS(self,
                      image: List[List[int]],
                      sr: int,
                      sc: int,
                      newColor: int) -> List[List[int]]:
        """
        T(n) = O(V + E) = O(n + 4n) = O(n) -- visit all nodes in worst case
        S(n) = O(n) -- size of queue
        """
        if newColor == image[sr][sc]:
            return image

        n, m = len(image), len(image[0])
        old_color = image[sr][sc]
        q = collections.deque()
        q.append((sr, sc))

        def neighbors(r, c):
            for (
                    new_r, new_c) in (
                    (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= new_r < n and 0 <= new_c < m and image[new_r][new_c] == old_color and (
                        new_r, new_c) not in q:
                    yield (new_r, new_c)

        while q:
            r, c = q.popleft()
            if image[r][c] == old_color:
                image[r][c] = newColor
            for (new_r, new_c) in neighbors(r, c):
                q.append((new_r, new_c))

        return image

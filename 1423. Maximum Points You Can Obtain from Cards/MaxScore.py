"""
There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        T(n) = O(K)
        S(n) = O(1)
        ----------
        use a sliding window of fixed size k to find the max range sum
        e.g. s = [1,2,3,4,5,6,1], k = 3
        first k iter: selected [5, 6, 1]
        k + 1 iter: selected [6,1,1] -> s = sum(5,6,1,1) - 5 = 8
        """
        res = s = 0
        for i in range(-k, k):
            s += cardPoints[i]
            if i >= 0:
                s -= cardPoints[i - k]
            res = max(res, s)
        return res
"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
"""
import collections


class Solution:
    def numTeams_cnt(self, rating: List[int]) -> int:
        """
        T(n) = O(n^2)
        S(n) = O(1)
        """
        if len(rating) < 3:
            return 0
        res = 0
        for i in range(len(rating)):
            # l = num of rating smaller than i on the left
            # r = ... greater on the right
            # l * r --> choose 1 from l and 1 from r to produce (l, i, r),
            # which is guranteed to be valid non-dec
            l = r = 0
            for j in range(i):
                if rating[i] > rating[j]:
                    l += 1
            for k in range(i + 1, len(rating)):
                if rating[i] < rating[k]:
                    r += 1
            # (i - l) = num greater on the left
            # (n - 1 - i - r) = num smaller on the right
            res += (l * r) + (i - l) * (len(rating) - 1 - i - r)
        return res

    def numTeams_BF(self, rating: List[int]) -> int:
        """
        T(n) = O(n^3)
        S(n) = O(1)
        """
        if len(rating) < 3:
            return 0
        res = 0
        for i, r1 in enumerate(rating):
            for j, r2 in enumerate(rating[i + 1:]):
                for k, r3 in enumerate(rating[i + j + 1:]):
                    if r1 < r2 < r3 or r1 > r2 > r3:
                        res += 1
        return res

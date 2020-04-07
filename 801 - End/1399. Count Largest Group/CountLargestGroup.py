"""
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.

Return how many groups have the largest size.
"""
from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        """
        T(n) = O(n) = 2n -- two for loops
        S(n) = O(n) -- size of map
        """
        mp = defaultdict(int)
        for i in range(1, n + 1):
            cur = 0
            num = i
            while num != 0:
                num, r = divmod(num, 10)
                cur += r
            mp[cur] += 1
        res = 0
        size = mp[max(mp, key=mp.get)]
        for v in mp.values():
            if v == size:
                res += 1
        return res

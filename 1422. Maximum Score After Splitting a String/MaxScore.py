"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
"""


from collections import Counter


class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):
            l = Counter(s[:i + 1])
            r = Counter(s[i + 1:])
            res = max(res, l['0'] + r['1'])
        return res

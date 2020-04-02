"""
Given a string, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        T(n) = O(n)
        S(n) = O(min(m,n)) n is the length of string and m is the size of character set
        """
        seen = {}
        start = max_len = 0
        for i, c in enumerate(s):
            if c in seen.keys() and start <= seen[c]:
                start = seen[c] + 1
            else:
                max_len = max(max_len, i - start + 1)
            seen[c] = i
        return max_len

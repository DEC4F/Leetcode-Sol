"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
"""
from collections import Counter, defaultdict
class Solution:
    def minWindow_sliding_window(self, s: str, t: str) -> str:
        """
        T(n) = O(n + m) -- n = len(s), m = len(t)
        S(n) = O(n + m) -- size of two dict
        """
        if not t or not s or len(s) < len(t):
            return ""
        if s == t:
            return s
        
        target_count = Counter(t)
        window_count = defaultdict(int)
        l, r = 0, 0
        formed = 0 # number of char in t satisfied in the window
        res = (float('inf'), l, r) # window length, l, r
        
        while r < len(s):
            char = s[r]
            window_count[char] += 1
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
                
            while l <= r and formed == len(target_count):
                char = s[l]
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                l += 1
                
            r += 1

        if res[0] == float('inf'):
            return ""
        return s[res[1] : res[2] + 1]
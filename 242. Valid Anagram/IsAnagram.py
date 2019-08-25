"""
Given two strings s and t , write a function to determine if t is an anagram of s.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        T(n) = O(n)
        S(n) = O(1) -- only 26 letters
        """
        seen = {}
        for c in s:
            if c in seen.keys():
                seen[c] += 1
            else:
                seen[c] = 1

        for c in t:
            if c not in seen.keys():
                return False
            else:
                seen[c] -= 1

        if not any(seen.values()):
            return True

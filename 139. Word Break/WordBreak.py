"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        T(n) = O(n^2) -- two loops checking prefixes
        S(n) = O(n) -- dp array
        """
        can_break_at = [False]*(len(s)+1)
        can_break_at[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if can_break_at[j] and s[j:i] in wordDict:
                    can_break_at[i] = True
                    break
        return can_break_at[len(s)]

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
"""

class Solution:
    def wordBreak_BF(self, s: str, wordDict: List[str]) -> List[str]:
        """
        T(n) = O(n^n) -- whyy
        S(n) = O(n^3) -- whyy
        """
        if not s or not wordDict:
            return []
        def rec(i: int) -> List[str]:
            res = []
            if i == len(s):
                res.append("")
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    lst = rec(j)
                    for l in lst:
                        if l == "":
                            res.append(s[i:j])
                        else:
                            res.append(s[i:j] + " " + l)
            return res
        return rec(0)

    def wordBreak_top_down(self, s: str, wordDict: List[str]) -> List[str]:
        """
        T(n) = O(n^3) -- whyy
        S(n) = O(n^3) -- whyy
        """
        if not s or not wordDict:
            return []
        seen_dict = {}
        def rec(i: int) -> List[str]:
            if i in seen_dict.keys():
                return seen_dict[i]
            res = []
            if i == len(s):
                res.append("")
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    lst = rec(j)
                    for l in lst:
                        if l == "":
                            res.append(s[i:j])
                        else:
                            res.append(s[i:j] + " " + l)
            seen_dict[i] = res
            return res
        return rec(0)

"""
Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
"""


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        """
        T(n) = O(n^2)
        S(n) = O(1)
        """
        res = []
        n = len(words)
        for w1 in words:
            for w2 in words:
                if w1 in w2 and w1 != w2:
                    res.append(w1)
                    break
        return res
"""
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.
"""


class Solution:
    def reformat(self, s: str) -> str:
        alphas = []
        digits = []
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                alphas.append(c)
        if abs(len(digits) - len(alphas)) > 1:
            return ""
        res = ''
        ll, sl = (
            digits, alphas) if len(alphas) < len(digits) else (
            alphas, digits)
        for i, j in zip(ll, sl):
            res += i
            res += j
        if len(ll) > len(sl):
            res += ll[-1]
        return res

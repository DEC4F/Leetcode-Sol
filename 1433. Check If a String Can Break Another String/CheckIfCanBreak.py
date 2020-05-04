"""
Given two strings: s1 and s2 with the same size, check if some permutation of string s1 can break some permutation of string s2 or vice-versa (in other words s2 can break s1).

A string x can break string y (both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0 and n-1.
"""


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        """
        T(n) = O(nlogn)
        S(n) = O(n)
        """
        if len(s1) != len(s1):
            return False
        s1, s2 = list(map(sorted, map(list, [s1, s2])))
        return all(
            ord(c1) >= ord(c2) for c1,
            c2 in zip(
                s1,
                s2)) or all(
            ord(c1) <= ord(c2) for c1,
            c2 in zip(
                s1,
                s2))

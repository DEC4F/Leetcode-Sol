"""
Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive) such that the denominator is less-than-or-equal-to n. The fractions can be in any order.
"""


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        """
        T(n) = O(n^2)
        S(n) = O(n^2)
        """
        res = {}
        for a in range(1, n):
            for b in range(a + 1, n + 1):
                f = a / b
                if f < 1 and res.get(frac) is None:
                    res[frac] = "{}/{}".format(a, b)
        return list(res.values())

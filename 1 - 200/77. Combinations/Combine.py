"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        T(n) = O()
        S(n) = O()
        """
        if n < 1 or n < k:
            return [[]]
        res = []
        def rec(idx, curr) -> None:
            if len(curr) == k:
                res.append(curr[:])
            for i in range(idx, n + 1):
                curr.append(i)
                rec(i + 1, curr)
                curr.pop()
        rec(1, [])
        return res

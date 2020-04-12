"""
Given the array queries of positive integers between 1 and m, you have to process all queries[i] (from i=0 to i=queries.length-1) according to the following rules:

In the beginning, you have the permutation P=[1,2,3,...,m].
For the current i, find the position of queries[i] in the permutation P (indexing from 0) and then move this at the beginning of the permutation P. Notice that the position of queries[i] in P is the result for queries[i].
Return an array containing the result for the given queries.
"""


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        """
        T(n) = O(m^2) = m*(2m)
        S(n) = O(n) -- size of P
        """
        P = [i + 1 for i in range(m)]
        res = []
        for q in queries:
            for i, n in enumerate(P):
                if n == q:
                    idx = i
                    break
            res.append(idx)
            # bubble up to front
            while idx != 0:
                P[idx] = P[idx - 1]
                idx -= 1
            P[idx] = q
        return res
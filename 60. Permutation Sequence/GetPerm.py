"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""


class Solution:
    def getPermutation_TLE(self, n: int, k: int) -> str:
        if n < 1:
            return ""
        nums = [i for i in range(1, n + 1)]
        perm = []
        used = [False] * n

        def rec(temp: List[int]) -> None:
            if len(temp) == n:
                perm.append(temp[:])
                return
            for i in range(n):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and used[i]):
                    continue
                used[i] = True
                temp.append(nums[i])
                rec(temp)
                used[i] = False
                temp.pop()
        rec([])
        return ''.join(str(e) for e in perm[k - 1])

    def getPermutation_fact_rep(self, n: int, k: int) -> str:
        """
        T(n) = O(n^2)
        S(n) = O(n)
        """
        f = [1] * n
        nums = ['1']
        for i in range(1, n):
            f[i] = f[i - 1] * i
            nums.append(str(i + 1))
        k -= 1
        res = []
        for i in range(n):
            idx = k // f[n - 1 - i]
            res.append(nums[idx])
            del nums[idx]
            k = k % int(f[n - 1 - i])
        return ''.join(res)

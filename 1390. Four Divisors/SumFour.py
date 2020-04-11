"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.
"""
from math import ceil, sqrt


class Solution:
    def sumFourDivisors_BF(self, nums: List[int]) -> int:
        """
        T(n) = O(VN) -- V is the max value N is the number of nums
        S(n) = O(V)
        """
        res = 0
        for n in nums:
            cnt, dsum = 2, 1 + n
            root = int(ceil(sqrt(n)))
            if root ** 2 == n:
                cnt += 1
                dsum += root
            for i in range(2, int(root)):
                d, r = divmod(n, i)
                if r == 0:
                    cnt += 2
                    dsum += d + i
                    if cnt > 4:
                        dsum = 0
                        break
            if cnt != 4:
                dsum = 0
            if dsum > 0:
                res += dsum
        return res
"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
"""

class Solution:
    def countBits_flip_and_count(self, num: int) -> List[int]:
        """
        T(n) = O(nk) -- k is num of 1-bit in n
        S(n) = O(n) -- output list
        """
        if num is None:
            return []

        def ham(n: int) -> int:
            w = 0
            while n != 0:
                n &= n - 1
                w += 1
            return w

        ans = []
        for i in range(num+1):
            ans.append(ham(i))
        return ans

    def countBits_dp(self, num: int) -> List[int]:
        """
        T(n) = O(n)
        S(n) = O(n)
        ----------
        ham weight of n is 1 more than ham weight of (n & (n - 1))
        since (n & (n - 1)) sets n's least sig 1-bit to 0
        """
        if num is None:
            return []
        ans = [0]*(num+1)
        for i in range(1, num+1):
            ans[i] = ans[i & (i-1)] + 1
        return ans

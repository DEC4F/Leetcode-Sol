"""
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight_mask(self, n: int) -> int:
        """
        T(n) = O(1) -- assumes n is a 32-bit int, loops every bit and checks for 1
        S(n) = O(1)
        """
        ans = 0
        mask = 1
        for _ in range(32):
            if (n & mask) != 0:
                ans += 1
            # shift mask to next bit
            mask <<= 1
        return ans

    def hammingWeight_flip_least_sig_one(self, n: int) -> int:
        """
        T(n) = O(1) -- faster than using 32-bit mask, even works for 64-bit int
        S(n) = O(1)
        ----------
        the least sig 1-bit will be flipped to 0 when we do (n & n-1)
        repeatedly doing it can reduce n to 0 (all 1-bit are flipped)
        """
        ans = 0
        while n != 0:
            n &= n - 1
            ans += 1
        return ans

"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
"""

class Solution:
    def addBinary_mod(self, a: str, b: str) -> str:
        """
        T(n) = O(n) = n+m -- one pass through each string
        S(n) = O(1) -- no extra space used
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        ans = []
        while i >= 0 or j >= 0:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            carry, bit = divmod(total, 2)
            ans.append(str(bit))
        if carry != 0:
            ans.append(str(carry))
        return ''.join(ans[::-1])
    
    def addBinary_BF(self, a: str, b: str) -> str:
        """
        T(n) = O(n) = n+ m + logn -- one pass for each num and logn for converting to binary
        S(n) = O(1) -- no extra memory used besides IO
        """
        if a == "0":
            return b
        elif b == "0":
            return a
        ans = self.binary_to_decimal(a) + self.binary_to_decimal(b)
        return decimal_to_binary(ans)
    
    def binary_to_decimal(self, a: str) -> int:
        n = 0
        for i in reversed(range(len(a))):
            if a[i] == '1':
                n += int(a[i])*2**(len(a) - 1 - i)
        return n

    def decimal_to_binary(self, a: int) -> str:
        bi = []
        while a != 0:
            a, r = divmod(a, 2)
            bi.insert(0, r)
        return ''.join([str(n) for n in bi])
    
    def addBinary_pythonic(self, a: str, b: str) -> str:
        """
        WON'T BE ACCEPTED IN INTERVIEW
        """
        return str(bin(int(a, 2) + int(b, 2)))[2:]
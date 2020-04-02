"""
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.

Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
"""


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        n_bytes = 0
        for n in data:
            b = format(n, '#010b')[-8:]
            if n_bytes == 0:
                while n_bytes < 8 and b[n_bytes] == '1':
                    n_bytes += 1
                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                if b[:2] != '10':
                    return False
            n_bytes -= 1
        return n_bytes == 0

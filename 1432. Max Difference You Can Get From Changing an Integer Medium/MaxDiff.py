"""
You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b.
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        a = b = str(num)
        for digit in a:
            if digit != '9':
                a = a.replace(digit, '9')
                break
        if b[0] != '1':
            b = b.replace(b[0], '1')
        else:
            for digit in b[1:]:
                if digit not in '01':
                    b = b.replace(digit, '0')
                    break
        return int(a) - int(b)
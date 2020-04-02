"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        if not digits:
            return []
        i = len(digits) - 1
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
        if i >= 0:
            digits[i] += 1
        else:
            digits.insert(0, 1)
        return digits

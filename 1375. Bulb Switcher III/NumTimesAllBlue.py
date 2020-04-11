"""
There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.
"""


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        right = res = 0
        for i, n in enumerate(light, 1):
            # keep track of the rightmost bulb
            right = max(right, n)
            # we have lit up i bulbs so far, if it happens to be equal to the
            # rightmost bulb, then all the ones to the left is lit up for sure
            if right == i:
                res += 1
        return res

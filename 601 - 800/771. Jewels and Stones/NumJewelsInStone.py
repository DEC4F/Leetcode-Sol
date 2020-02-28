"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""
from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        """
        T(n) = O(n + m)
        S(n) = O(n)
        """
        if not J or not S:
            return 0
        res = 0
        c = Counter(S)
        for t in J:
            res += c[t]
        return res
"""
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.
"""
from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        """
        T(n) = O(nlogn) = nlogn + n + n
        S(n) = O(n)
        """
        mp = sorted([[k, v]
                     for k, v in Counter(s).items()], key=lambda x: x[0])
        res = ''
        while len(res) < len(s):
            for i, (char, cnt) in enumerate(mp):
                if cnt:
                    mp[i][1] -= 1
                    res += char
            for i in range(len(mp)):
                char = mp[~i][0]
                cnt = mp[~i][1]
                if cnt:
                    mp[~i][1] -= 1
                    res += char
        return res

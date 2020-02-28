"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        r_count = l_count = 0
        ans = 0
        for c in s:
            if c == 'R':
                r_count += 1
            else:
                l_count += 1
            if r_count - l_count == 0:
                ans += 1
                r_count, l_count = 0, 0
        return ans
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        T(n) = O()
        S(n) = O()
        """
        res = []
        def rec(s: int, opened: int, closed: int) -> int:
            if len(s) == 2 * n:
                res.append(s)
                return
            if opened < n:
                rec(s + '(', opened + 1, closed)
            if closed < opened:
                rec(s + ')', opened, closed + 1)
        rec('', 0, 0)
        return res
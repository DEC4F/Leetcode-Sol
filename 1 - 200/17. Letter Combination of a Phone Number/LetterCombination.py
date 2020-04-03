"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


class Solution:

    def __init__(self):

        self.keyboard = {'2': ['a', 'b', 'c'],
                         '3': ['d', 'e', 'f'],
                         '4': ['g', 'h', 'i'],
                         '5': ['j', 'k', 'l'],
                         '6': ['m', 'n', 'o'],
                         '7': ['p', 'q', 'r', 's'],
                         '8': ['t', 'u', 'v'],
                         '9': ['w', 'x', 'y', 'z']
                         }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        T(n) = O(3^m + 4^n)
        S(n) = O(log(m+n))
        """
        ans = []
        if not digits:
            return ans

        def recur(current, remains):
            if not remains:
                ans.append(current)
            else:
                for c in self.keyboard[remains[0]]:
                    recur(current + c, remains[1:])

        recur("", digits)
        return ans

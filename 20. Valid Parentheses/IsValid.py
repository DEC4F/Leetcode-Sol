"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution:
    """
    T(n) = O(n) -- one pass
    S(n) = O(n) -- stored a stack
    """

    def isValid(self, s: str) -> bool:
        parens = {'(': ')', '{': '}', '[': ']'}
        open_brackets = ['(', '{', '[']
        stack = []

        for paren in s:
            if paren in open_brackets:
                stack.append(paren)
            elif stack and paren == parens[stack[-1]]:
                stack.pop()
            else:
                return False

        return len(stack) == 0

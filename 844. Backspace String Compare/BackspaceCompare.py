"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
"""
from itertools import zip_longest


class Solution:
    def backspaceCompare_stack(self, S: str, T: str) -> bool:
        """
        T(n) = O(n + m)
        S(n) = O(n + m)
        """
        def process(s: str) -> List[str]:
            stack = []
            for c in s:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        return process(S) == process(T)

    def backspaceCompare_ptr(self, S: str, T: str) -> bool:
        """
        T(n) = O(n + m)
        S(n) = O(1)
        """
        def char_gen(s):
            skip = 0
            for c in reversed(s):
                if c == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    yield c
        return all(s == t for s, t in zip_longest(char_gen(S), char_gen(T)))
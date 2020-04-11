"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        T(n) = 3n = O(n) -- lower() and upper() takes O(n) times
        S(n) = O(1) -- only stored boolean result, const space
        """
        if not word or len(word) < 2:
            return True
        upper = word.upper() == word
        lower = word.lower() == word
        title = word[0].upper() + word[1:].lower() == word
        return upper or lower or title

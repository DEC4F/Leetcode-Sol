"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        T(n) = O(nm) -- n is number of words, m is average length of a word
        S(n) = O(c) -- c is number of char in the alphabet, used a hash map to store the index
        """
        if len(words) <= 1:
            return True
        # {character : index in alphabet}
        ord_dict = {c: i for i, c in enumerate(order)}
        if len(words) == 2:
            return self.isAdjacentWordsSorted(words[0], words[1], ord_dict)
        for i in range(len(words) - 2):
            if not self.isAdjacentWordsSorted(
                    words[i], words[i + 1], ord_dict):
                return False
        return True

    def isAdjacentWordsSorted(
            self,
            word1: str,
            word2: str,
            ord_dict: dict) -> bool:
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if ord_dict[word1[j]] < ord_dict[word2[j]]:
                    break
                return False
            if word2 in word1:
                return False
        return True

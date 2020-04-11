"""
Given an array of strings, group anagrams together.
"""


class Solution:
    def groupAnagrams_sorting(self, strs: List[str]) -> List[List[str]]:
        """
        T(n) = O(nklogk) -- k is max length of a word: sort word takes klogk times, and we did it for each word in the list
        S(n) = O(nk) -- stored sorted letters and word list pair in dict
        """
        anagrams = {}
        for word in strs:
            letters = ''.join(sorted(list(word)))
            if letters in anagrams.keys():
                anagrams[letters].append(word)
            else:
                anagrams[letters] = [word]
        return anagrams.values()

    def groupAnagrams_ord_mask(self, strs: List[str]) -> List[List[str]]:
        """
        T(n) = O(nk) -- one pass for each word and one pass for each char
        S(n) = O(nk) -- stored all masks and words in one hash table
        """
        anagrams = {}
        for word in strs:
            mask = [0] * 26
            for c in word:
                mask[ord(c) - ord('a')] += 1
            mask_as_key = tuple(mask)
            if mask_as_key in anagrams.keys():
                anagrams[mask_as_key].append(word)
            else:
                anagrams[mask_as_key] = [word]
        return anagrams.values()

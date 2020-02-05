"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        T(n) = O(mn) -- time to build 2 defaultdict as well as filling in values, where n is the num of words and m is the max length of a word
        S(n) = O(mn) -- size of dicts and queue in worst case
        """
        res = ""
        if not words or len(words) < 1:
            return res
        # to store all the letters that come after current key letter
        set_letters_after_key = {}
        # to store number of letters came before current key letter
        num_letters_before_key = {}
        for word in words:
            for char in word:
                set_letters_after_key[char] = set()
                num_letters_before_key[char] = 0

        # filling in values for both dicts
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(min(len(word1), len(word2))):
                let1, let2 = word1[j], word2[j]
                if let1 != let2:
                    if let2 not in set_letters_after_key[let1]:
                        set_letters_after_key[let1].add(let2)
                        num_letters_before_key[let2] += 1
                    break

        # store all "head" letters in the queue, and do topological sort
        queue = collections.deque()
        for c in num_letters_before_key.keys():
            if num_letters_before_key[c] == 0:
                queue.append(c)
        while queue:
            c1 = queue.popleft()
            res += c1
            for c2 in set_letters_after_key[c1]:
                num_letters_before_key[c2] -= 1
                if num_letters_before_key[c2] == 0:
                    queue.append(c2)
        
        if len(res) != len(num_letters_before_key):
            return ""
        return res
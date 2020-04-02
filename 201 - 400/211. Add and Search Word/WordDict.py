class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_end = False


class WordDictionary_REC:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.

        T(n) = O(L) -- L is the length of the word
        S(n) = O(1)
        """
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.is_end = True

    def search_rec(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.

        T(n) = O(n)
        S(n) = O(n)
        """
        self.res = False
        node = self.root
        self.rec_search(word, node)
        return self.res

    def rec_search(self, word: str, node: TrieNode):
        if not word:
            if node.is_end:
                self.res = True
            return
        if word[0] == '.':
            for child_node in node.children.values():
                self.rec_search(word[1:], child_node)
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.rec_search(word[1:], node)

    def search_iter(self, word: str) -> bool:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        stack = [(word, self.root)]
        while stack:
            w, node = stack.pop()
            if not w:
                if node.is_end:
                    return True
            elif w[0] == '.':
                for child_node in node.children.values():
                    stack.append((w[1:], child_node))
            else:
                node = node.children.get(w[0])
                if node is not None:
                    stack.append((w[1:], node))
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

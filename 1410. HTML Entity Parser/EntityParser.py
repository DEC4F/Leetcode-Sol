"""
HTML entity parser is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

Quotation Mark: the entity is &quot; and symbol character is ".
Single Quote Mark: the entity is &apos; and symbol character is '.
Ampersand: the entity is &amp; and symbol character is &.
Greater Than Sign: the entity is &gt; and symbol character is >.
Less Than Sign: the entity is &lt; and symbol character is <.
Slash: the entity is &frasl; and symbol character is /.
Given the input text string to the HTML parser, you have to implement the entity parser.

Return the text after replacing the entities by the special characters.
"""


class Solution:
    def entityParser(self, text: str) -> str:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        mp = {'&frasl;': '/',
              '&quot;': '\"',
              '&apos;': '\'',
              '&amp;' : '&',
              '&gt;'  : '>',
              '&lt;'  : '<'
             }
        i = 0
        while i < len(text):
            if text[i] == '&':
                for j in range(4, 9):
                    if mp.get(text[i:i + j]) is not None:
                        text = text[:i] + mp[text[i:i + j]] + text[i + j:]
            i += 1
        return text
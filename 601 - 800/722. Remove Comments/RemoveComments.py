"""
Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code. This represents the result of splitting the original source code string by the newline character \n.

In C++, there are two types of comments, line comments, and block comments.

The string // denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.

The string /* denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of */ should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.

The first effective comment takes precedence over others: if the string // occurs in a block comment, it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored.

If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters. For example, source = "string s = "/* Not a comment. */";" will not be a test case. (Also, nothing else such as defines or macros will interfere with the comments.)

It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.
"""


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        flg = False
        cur_line = ''
        res = []
        for line in source:
            if not flg:
                cur_line = ''
            i = 0
            while i < len(line):
                # start block comment
                if line[i : i + 2] == '/*' and not flg:
                    flg = True
                    i += 1

                # end block comment
                elif line[i : i + 2] == '*/' and flg:
                    flg = False
                    i += 1

                # ignore the rest of the line if seen //
                elif line[i : i + 2] == '//' and not flg:
                    break

                elif not flg:
                    cur_line += line[i]

                i += 1

            if cur_line and not flg:
                    res.append(cur_line)

        return res
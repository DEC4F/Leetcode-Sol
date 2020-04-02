"""
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy.
"""


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        """
        T(n) = O(nk) -- K is size of max word length
        S(n) = O(k) -- max size of group and size array
        """
        if not S or not words:
            return 0

        def group(s):
            group = [s[0]]
            size = [1]
            for c in s[1:]:
                if c == group[-1]:
                    size[-1] += 1
                else:
                    group.append(c)
                    size.append(1)
            return group, size

        res = 0
        target_group, target_size = group(S)

        for w in words:
            cur_group, cur_size = group(w)
            if target_group != cur_group:
                continue
            res += all(t == c or t >= max(c, 3)
                       for t, c in zip(target_size, cur_size))
        return res

"""
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
"""


class Solution:
    def getHappyString_vanilla(self, n: int, k: int) -> str:
        """
        T(n) = O(2^n)
        S(n) = O(n)
        """
        if k > 3 * 2 ** (n - 1):
            return ""

        def backtrack(happy_str: List[str], prev: str):
            if len(happy_str) == n:
                self.all_str.append(''.join(happy_str))
                return
            for let in ('a', 'b', 'c'):
                if prev == let:
                    continue
                happy_str.append(let)
                backtrack(happy_str, let)
                happy_str.pop()
        self.all_str = []
        backtrack([], '')
        self.all_str.sort()
        return self.all_str[k - 1]

    def getHappyString_fast(self, n: int, k: int) -> str:
        n_total = 2 ** (n - 1)
        if k > 3 * n_total:
            return ""
        res = prev = ""
        prev += "abc"[(k - 1) // n_total]
        mp = {
            "a": ["b", "c"],
            "b": ["a", "c"],
            "c": ["a", "b"]
        }
        while n_total > 0:
            res += prev
            k -= n_total * ((k - 1) // n_total)
            n_total //= 2
            if k <= n_total:
                prev = mp[prev][0]
            else:
                prev = mp[prev][1]
        return res


a = Solution()
a.getHappyString_fast(3, 9)

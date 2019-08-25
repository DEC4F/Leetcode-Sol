class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        T(n) = O(n^2)
        S(n) = O(1)
        """
        if len(s) < 2:
            return s
        lo = 0
        max_len = 0
        for i in range(len(s)):
            odd_len = self.palindrome_len_at(s, i, i)
            even_len = self.palindrome_len_at(s, i, i+1)
            if max(odd_len, even_len) > max_len:
                if odd_len >= even_len:
                    lo = i - odd_len//2
                    max_len = odd_len
                else:
                    lo = i - even_len//2 + 1
                    max_len = even_len
        return s[lo:lo + max_len]

    def palindrome_len_at(self, s: str, j: int, k: int) -> int:
        while (j >= 0 and k < len(s) and s[j] == s[k]):
            j -= 1
            k += 1
        return k - j - 1

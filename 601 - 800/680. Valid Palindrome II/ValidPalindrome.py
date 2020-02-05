class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        T(n) = O(n) -- visit each char at most twice
        S(n) = O(1)
        """
        if len(s) < 2:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.is_palindromic(s, l + 1, r) or self.is_palindromic(s, l, r - 1)
        return True
    
    def is_palindromic(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
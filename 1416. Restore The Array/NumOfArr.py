"""
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k. There can be multiple ways to restore the array.

Return the number of possible array that can be printed as a string s using the mentioned program.

The number of ways could be very large so return it modulo 10^9 + 7
"""


class Solution:
    def numberOfArrays_memo(self, s: str, k: int) -> int:
        """
        T(n) = O(nlog(10)k) = O(n) -- log(10)k is number of digits in k
        S(n) = O(n)
        """
        mod = 10 ** 9 + 7

        def dp(i: int, memo) -> int:
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if memo[i] != 0:
                return memo[i]
            num_ij = 0
            for j in range(i, len(s)):
                num_ij = num_ij * 10 + int(s[j])
                if num_ij <= k:
                    memo[i] += dp(j + 1, memo)
                    memo[i] %= mod
                else:
                    break
            return memo[i]
        return dp(0, [0] * len(s))

    def numberOfArrays_dp_arr(self, s: str, k: int) -> int:
        """
        T(n) = O(nlog(10)k)
        S(n) = O(n)
        ------------
        dp[n] = 1
        dp[i] = sum(dp[j] for all j s.t. 1 <= s[i:j] <= k)
        """
        n = len(s)
        mod = 10 ** 9 + 7
        dp = [0] * n + [1]
        for i in range(n - 1, -1, -1):
            num = int(s[i])
            for j in range(i + 1, n + 1):
                if 1 <= num <= k:
                    dp[i] += dp[j]
                    dp[i] %= mod
                    if j < n:
                        num = 10 * num + int(s[j])
                else:
                    break
        return dp[0]


a = Solution()
a.numberOfArrays_memo("1000", 10000)
a.numberOfArrays_dp_arr("1000", 10000)

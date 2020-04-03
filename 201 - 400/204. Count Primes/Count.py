"""
Count the number of prime numbers less than a non-negative number, n.
"""


class Solution:
    def countPrimes_TLE(self, n: int) -> int:
        """
        T(n) = O(n^1.5) -- O(n) to determine is prime and O(n) to count all smaller primes
        S(n) = O(1)
        """
        def is_prime(num: int) -> bool:
            i = 2
            while i**2 <= num:
                if num % i == 0:
                    return False
                i += 1
            return True
        res = 0
        for i in range(2, n):
            if is_prime(i):
                res += 1
        return res

    def countPrimes_Sieve_of_Eratosthenes(self, n: int) -> int:
        """
        T(n) = O(n) to mark off all the multiples of primes that has been found
        S(n) = O(n) -- size of res
        """
        if n == 0:
            return 0
        if n == 1:
            return 0
        res = [1] * n
        i = 2
        while i ** 2 < n:
            if res[i]:
                j = i ** 2
                while j < n:
                    res[j] = 0
                    j += i
            i += 1
        return sum(res) - 2  # exclude 0 and 1

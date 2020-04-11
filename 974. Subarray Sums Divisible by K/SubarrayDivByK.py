from collections import Counter


class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        """
        T(n) = O(N + K) = 2N + K -- one
        S(n) = O(N) -- prefix sum array
        ---------
        building prefix sum array % K
        every two pair of same r mod K value cancels out leaves 0 mod K range sum
        """
        prefix = [0]
        for n in A:
            prefix.append((prefix[-1] + n) % K)
        counter = Counter(prefix).values()
        return sum(c * (c - 1) // 2 for c in counter)

    def subarraysDivByK_one_pass(self, A: List[int], K: int) -> int:
        """
        T(n) = O(n)
        S(n) = O(K)
        ---------
        squash prefix sum array to one variable
        """
        res = 0
        prefix = 0
        count = [1] + [0] * K
        for n in A:
            prefix = (prefix + n) % K
            res += count[prefix]
            count[prefix] += 1
        return res

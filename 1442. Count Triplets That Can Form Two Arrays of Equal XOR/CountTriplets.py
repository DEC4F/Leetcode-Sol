class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        res = cur = 0
        count = {0 : [1, 0]}
        for i, a in enumerate(arr):
            cur ^= a
            n, total = count.get(cur, [0, 0])
            res += i * n - total
            count[cur] = [n + 1, total + i + 1]
        return res

    def countTriplets_prefix(self, arr: List[int]) -> int:
        """
        T(n) = O(n^2)
        S(n) = O(n)
        """
        res = 0
        prefix = [0] # len = n + 1
        for i in range(len(arr)):
            prefix.append(prefix[-1] ^ arr[i])
        for i in range(len(arr) + 1):
            for k in range(i + 1, len(arr) + 1):
                if prefix[i] == prefix[k + 1]:
                    res += k - i
        return res

    def countTriplets_BF_TLE(self, arr: List[int]) -> int:
        """
        T(n) = O(n^4)
        S(n) = O(1)
        """
        from functools import reduce
        res = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    a = reduce((lambda x, y : x ^ y), arr[i : j])
                    b = reduce((lambda x, y : x ^ y), arr[j : k + 1])
                    if a == b:
                        res += 1
        return res
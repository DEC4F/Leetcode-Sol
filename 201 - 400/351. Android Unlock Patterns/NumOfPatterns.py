"""
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:
- Each pattern must connect at least m keys and at most n keys.
- All the keys must be distinct.
- If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
- The order of keys used matters.
"""
class Solution:

    def __init__(self):
        self.illegals = {
            1: { 2: None, 5: None, 4: None, 6: None, 8: None, 3: 2, 7: 4, 9: 5 },
            2: { 1: None, 5: None, 4: None, 6: None, 3: None, 9: None, 7: None, 8: 5 },
            3: { 2: None, 5: None, 6: None, 4: None, 8: None, 7: 5, 1: 2, 9: 6 },
            4: { 1: None, 7: None, 2: None, 5: None, 8: None, 9: None, 3: None, 6: 5 },
            5: { 1: None, 2: None, 3: None, 4: None, 6: None, 7: None, 8: None, 9: None },
            6: { 3: None, 9: None, 2: None, 5: None, 8: None, 1: None, 7: None, 4: 5 },
            7: { 4: None, 5: None, 8: None, 6: None, 2: None, 9: 8, 1: 4, 3: 5 },
            8: { 4: None, 5: None, 6: None, 7: None, 9: None, 1: None, 3: None, 2: 5 },
            9: { 8: None, 5: None, 6: None, 4: None, 2: None, 7: 8, 1: 5, 3: 6 }
        }
        self.memo = {}
        self.res = 0

    def numberOfPatterns_DP_top_down(self, m: int, n: int) -> int:
        """
        T(n) = O(n^2) = 1 + 2 + ... + n
        S(n) = O(n)
        """
        if not (1 <= m <= n <= 9):
            return 0
        res = 0

        def backtrack(used: List[bool], key: int, k: int) -> int:
            if k == 1:
                return 1
            comb = tuple(used), key, k
            if comb in self.memo:
                return self.memo[comb]
            self.memo[comb] = 0

            for idx, next_key in enumerate([i for i in range(1, 10)]):
                if next_key == key or used[idx]:
                    continue
                if self.illegals[key].get(next_key) and not used[self.illegals[key].get(next_key) - 1]:
                    continue
                used[idx] = True
                self.memo[comb] += backtrack(used, next_key, k - 1)
                used[idx] = False
            return self.memo[comb]

        for k in range(m, n + 1):
            for i, key in enumerate([i for i in range(1, 10)]):
                used = [False] * 9
                used[i] = True
                res += backtrack(used, key, k)
        return res

    def numberOfPatterns_backtrack(self, m: int, n: int) -> int:
        """
        T(n) = O(n!) -- backtrack to generate all combination
        S(n) = O(n) -- size of used array
        """
        if not(1 <= m <= n <= 9):
            return 0
        used = [False] * 9

        def backtrack(comb: List[int], k: int) -> None:
            if len(comb) == k:
                self.res += 1
                return
            for key in range(1, 10):
                if used[key - 1]:
                    continue
                if comb and self.illegals[comb[-1]].get(key) and self.illegals[comb[-1]].get(key) not in comb:
                    continue
                used[key - 1] = True
                comb.append(key)
                backtrack(comb, k)
                comb.pop()
                used[key - 1] = False

        for i in range(m, n + 1):
            backtrack([], i)
        return self.res

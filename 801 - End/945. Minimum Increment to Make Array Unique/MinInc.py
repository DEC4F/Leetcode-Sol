"""
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.
"""
class Solution:
    def minIncrementForUnique_list(self, A: List[int]) -> int:
        """
        T(n) = O(n) = n + c * c = O(n)
        S(n) = O(n) -- size of count
        """
        count = collections.Counter(A)
        taken = []
        ans = 0

        for i in range(100000):
            if count[i] > 1:
                for _ in range(count[i] - 1):
                    taken.append(i)
            elif len(taken) > 0 and count[i] == 0:
                ans += i - taken.pop()

        return ans

    def minIncrementForUnique_sort(self, A):
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in range(1, len(A)):
            if A[i - 1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                # give is the number of dup that can be inserted into this interval
                give = min(taken, A[i] - A[i - 1] - 1)
                # sum (A[i - 1] + 1, A[i - 1] + 2, ..., A[i - 1] + give)
                ans += (give * (give + 1) / 2) + give * A[i - 1]
                taken -= give

        return int(ans)

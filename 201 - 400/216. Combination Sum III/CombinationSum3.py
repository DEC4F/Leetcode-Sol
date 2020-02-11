"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(path: List[int], start: int, k: int, n: int) -> None:
            if k < 0 or n < 0:
                return
            if k == 0 and n == 0:
                ans.append(path[:])
                return
            for i in range(start, 10):
                path.append(i)
                dfs(path, i + 1, k - 1, n - i)
                path.pop()
        
        dfs([], 1, k, n)
        return ans
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
"""

class Solution:
    def permuteUnique_memo(self, nums: List[int]) -> List[List[int]]:
        """
        T(n) = O()
        S(n) = O()
        """
        if nums is None:
            return [[]]
        nums.sort()
        res = []
        used = [False]*len(nums)
        def rec(temp) -> None:
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and used[i - 1]):
                    continue
                used[i] = True
                temp.append(nums[i])
                rec(temp)
                used[i] = False
                temp.pop()
        rec([])
        return res

    def permuteUnique_iter(self, nums: List[int]) -> List[List[int]]:
        """
        T(n) = O()
        S(n) = O()
        """
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n: 
                        break
            ans = new_ans
        return ans
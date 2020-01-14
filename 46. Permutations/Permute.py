"""
Given a collection of distinct integers, return all possible permutations.
"""

class Solution:
    def permute_memo(self, nums: List[int]) -> List[List[int]]:
        """
        T(n) = O()
        S(n) = O()
        """
        if nums is None:
            return []
        res = []
        used = [False]*len(nums)
        def rec(temp: List[int]) -> None:
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                temp.append(nums[i])
                rec(temp)
                temp.pop()
                used[i] = False
        rec([])
        return res

    def permute_swap(self, nums: List[int]) -> List[List[int]]:
        """
        T(n) = O()
        S(n) = O()
        """
        res = []
        def rec(first: int) -> None:
            if first == len(nums):
                res.append(nums[:])
                return
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                rec(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        rec(0)
        return res
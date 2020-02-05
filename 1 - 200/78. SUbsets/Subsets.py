"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        def rec(card: int, idx: int, cur_subset: List[int]) -> None:
            if len(cur_subset) == card:
                res.append(cur_subset[:])
            for i in range(idx, len(nums)):
                cur_subset.append(nums[i])
                rec(card, i + 1, cur_subset)
                cur_subset.pop()
        for card in range(len(nums) + 1):
            rec(card, 0, [])
        return res

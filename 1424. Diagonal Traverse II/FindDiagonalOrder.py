"""
Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.

Input: nums = [[1,2,3],
               [4,5,6],
               [7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
"""


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        res = []
        for i, row in enumerate(nums):
            for j, n in enumerate(row):
                if len(res) <= i + j:
                    res.append([])
                res[i + j].append(n)
        """
        res = [[1],
               [2,4],
               [3,5,7],
               [6,8],
               [9]]
        """
        return [n for r in res for n in reversed(r)]
"""
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.
"""
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        if len(nums) < 3:
            return False

        count_map = collections.Counter(nums)
        hypo_map = collections.defaultdict(int)

        for n in nums:
            if count_map[n] == 0:
                continue
            if hypo_map[n] > 0:
                hypo_map[n] -= 1
                hypo_map[n + 1] += 1
                count_map[n] -= 1
            else:
                if all(c > 0 for c in [count_map[n + i] for i in range(3)]):
                    count_map[n] -= 1
                    count_map[n + 1] -= 1
                    count_map[n + 2] -= 1
                    hypo_map[n + 3] += 1
                else:
                    return False
        return True
"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.linearSelect(nums, len(nums) - k)

    def linearSelect(self, nums: List[int], k: int) -> int:
        """
        T(n) = T(ceil(n/5)) + T(1 - 3*(1/2*ceil(n/5)-2)) + cn
             recursive call     call on lower/upper     partition
             <= T(n/5) + T(7n/10) + cn
             < O(n) by recursion tree analysis

        S(n) = O(n) -- used extra lists to store entire input array
        """
        n = 5
        if len(nums) <= n + 1:
            return sorted(nums)[k]

        # divide into groups of 5
        grouped_nums = []
        left_idx = 0
        while left_idx + n < len(nums) - 1:
            grouped_nums.append(nums[left_idx:left_idx + n])
            left_idx += n
        grouped_nums.append(nums[left_idx:])

        # recursively find medians of median
        medians = []
        for group in grouped_nums:
            medians.append(self.linearSelect(group, (len(group) - 1) // 2))
        med_of_med = self.linearSelect(medians, (len(medians) - 1) // 2)

        # categorize values into 3 sublist
        lower = []
        equal = []
        higher = []
        for n in nums:
            if n < med_of_med:
                lower.append(n)
            elif n > med_of_med:
                higher.append(n)
            else:
                equal.append(n)
        if k < len(lower):
            return self.linearSelect(lower, k)
        elif k < len(equal) + len(lower):
            return equal[0]
        else:
            return self.linearSelect(higher, k - len(equal) - len(lower))

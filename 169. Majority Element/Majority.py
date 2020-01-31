class Solution:
    def majorityElement_divide_n_conquer(self, nums: List[int]) -> int:
        """
        T(n) = O(nlogn) = 2T(n/2) + n
        S(n) = O(logn)
        """
        def rec(lo: int, hi: int) -> int:
            if lo == hi:
                return nums[lo]
            mid = (lo + hi) // 2
            left = rec(lo, mid)
            right = rec(mid + 1, hi)
            # if left&right subarray agrees on the majority value, return it
            if left == right:
                return left
            # if disagree, combine the two and count the majority element
            l_sum = r_sum = 0
            for i in range(lo, hi + 1):
                if nums[i] == left:
                    l_sum += 1
                elif nums[i] == right:
                    r_sum += 1
            if r_sum > l_sum:
                return right
            return left
        return rec(0, len(nums) - 1)

    def majorityElement_randomized(self, nums: List[int]) -> int:
        """
        T(n) = O(infinity) in worst case, O(n) on average case with a probability of 1/2
        S(n) = O(1)
        """
        import random
        thresh = len(nums) // 2
        while True:
            m = random.choice(nums)
            if sum(1 for n in nums if n == m) > thresh:
                return m

    def majorityElement_sorting(self, nums: List[int]) -> int:
        """
        T(n) = O(nlogn) -- sorting
        S(n) = O(1)
        ----------
        since we have a majority, it's guranteed to occupy the middle index
        """
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement_hash(self, nums: List[int]) -> int:
        """
        T(n) = O(n) -- max function, building counter
        S(n) = O(n) -- size of hash table
        """
        from collections import Counter
        c = Counter(nums)
        return max(c.keys(), key=c.get)

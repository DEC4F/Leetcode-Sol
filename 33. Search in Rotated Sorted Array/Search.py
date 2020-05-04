"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""


class Solution:
    class Solution:

    def search(self, nums: List[int], target: int) -> int:
        """
        T(n) = O(logn)
        S(n) = O(1)
        """
        if len(nums) < 1:
            return -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            # lo .. mid .. pivot .. hi
            elif nums[mid] >= nums[lo]:
                # lo .. target .. mid .. pivot .. hi
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                # lo .. mid .. target .. pivot .. hi
                # or
                # lo .. mid .. pivot .. target .. hi
                else:
                    lo = mid + 1
            # lo .. pivot .. mid .. hi
            else:
                # lo .. pivot .. mid .. target .. hi
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                # lo .. target .. pivot .. mid .. hi
                # or
                # lo .. pivot .. target .. mid .. hi
                else:
                    hi = mid - 1
        return -1

    def search_recur(self, nums: List[int], target: int) -> int:
        """
        T(n) = O(logn) -- recursive binary search
        S(n) = O(logn) -- recursion stack size
        """
        if nums is None or nums == []:
            return -1

        def search_(self, nums: List[int], l: int, r: int, target: int) -> int:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if r < l:
                return -1
            # if leftend is smaller than mid, then pivot is on the right
            if nums[l] < nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    return self.search_(nums, l, mid - 1, target)
                else:
                    return self.search_(nums, mid + 1, r, target)
            # when leftend greater than mid, pivot on the left
            elif nums[l] > nums[mid]:
                if target >= nums[mid] and target <= nums[r]:
                    return self.search_(nums, mid + 1, r, target)
                else:
                    return self.search_(nums, l, mid - 1, target)
            # all repeated elements on the left
            elif nums[l] == nums[mid]:
                # if no repeated elements on the right
                if nums[r] != nums[mid]:
                    # search rightside
                    return self.search_(nums, mid + 1, r, target)
                else:
                    # both full of repeated elements, search both sides
                    temp = self.search_(nums, l, mid - 1, target)
                    if temp == -1:
                        return self.search_(nums, mid + 1, r, target)
                    else:
                        return temp
            return -1

        return self.search_(nums, 0, len(nums) - 1, target)

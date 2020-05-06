"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
"""


from heapq import heappush, heappop


class Solution:
    def kSmallestPairs_merge(self, nums1: List[int],
                                   nums2: List[int],
                                   k: int) -> List[List[int]]:
        """
        T(n) = O(klogk) -- only compute the top k sums in pq
        S(n) = O(k) -- max size of pq is k
        """
        if not nums1 or not nums2 or not k:
            return []
        pq = []
        i = 0
        while i < len(nums1) and i < k:
            heappush(pq, (nums1[i] + nums2[0],
                          nums1[i],
                          nums2[0],
                          0))
            i += 1
        res = []
        while pq and len(res) < k:
            cur_tp = heappop(pq)
            res.append([cur_tp[1], cur_tp[2]])
            if cur_tp[-1] != len(nums2) - 1:
                n1, n2 = cur_tp[1], nums2[cur_tp[-1] + 1]
                heappush(pq, (n1 + n2, n1, n2, cur_tp[-1] + 1))
        return res

    def kSmallestPairs_heapsort(self, nums1: List[int],
                                      nums2: List[int],
                                      k: int) -> List[List[int]]:
        """
        T(n) = O(mn + k) -- computed entire table
        S(n) = O(mn)
        """
        if not nums1 or not nums2 or not k:
            return []
        pq = []
        for n1 in nums1:
            for n2 in nums2:
                heappush(pq, (n1 + n2, n1, n2))
        res = []
        while pq and len(res) < k:
            res.append(list(heappop(pq)[1:]))
        return res
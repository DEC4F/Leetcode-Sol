class Solution:

    def kClosest_sort(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        T(n) = O(nlogn)
        """
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:K]

    def dist(self, coord1: List[int]) -> int:
        return (coord1[0]**2) + (coord1[1]**2)

    def select(self, points: List[List[int]], K: int) -> List[List[int]]:
        # group of 5
        groups = []
        l = 0
        while l+5 < len(points)-1:
            groups.append(points[l:l+5])
            l += 5
        groups.append(points[l:])

        # median of medians
        medians = []
        for group in groups:
            medians.append(self.select(group, (len(group)+1)//2))
        med_dist = self.dist(self.select(medians, (len(medians)+1)//2))
        
        lower = []
        higher = []
        eq = []
        for point in points:
            curr_dist = self.dist(point)
            if curr_dist < med_dist:
                lower.append(point)
            elif curr_dist > med_dist:
                higher.append(point)
            else:
                eq.append(point)
        if K < len(lower):
            return self.select(lower, K)
        elif K < len(lower) + len(eq):
            return eq[0]
        else:
            return self.select(higher, K-len(lower)-len(eq))

    def kClosest_DC(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        T(n) = O(n)
        """
        if len(points) <= K:
            return points
        else:
            return self.select(points, K)
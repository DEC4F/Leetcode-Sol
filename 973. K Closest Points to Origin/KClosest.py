class Solution:

    def dist(self, point: List[int]) -> int:
        return point[0]**2 + point[1]**2

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        T(n) = O(n) -- linear time
        S(n) = O(n) -- recursion stack in worst case (inversely sorted)
        """
        if len(points) <= K:
            return points

        def sort(l: int, r: int, K: int):
            if l >= r:
                return None
            pivot = random.randint(l, r)
            points[l], points[pivot] = points[pivot], points[r]

            mid = partition(l, r)
            if K < mid-l+1:
                sort(l, mid-1, K)
            elif K > mid-l+1:
                sort(mid+1, r, K - (mid-l+1))

        def partition(l: int, r: int) -> int:
            pivot =  l
            pivot_dist = self.dist(points[pivot])
            l += 1
            while True:
                while l < r and self.dist(points[l]) < pivot_dist:
                    l += 1
                while l <= r and self.dist(points[r]) >= pivot_dist:
                    r -= 1
                if l >= r:
                    break
                points[l], points[r] = points[r], points[l]
            points[pivot],  points[r] = points[r], points[pivot]
            return r

        sort(0, len(points)-1, K)
        return points[:K]

    def kClosest_DC(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        T(n) = O(n)
        """
        if len(points) <= K:
            return points
        else:
            return self.select(points, K)

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

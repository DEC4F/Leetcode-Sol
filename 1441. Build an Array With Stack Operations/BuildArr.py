class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
        T(n) = O(n)
        S(n) = O(1)
        """
        res = []
        i = 1
        for n in target:
            while i < n:
                res.append("Push")
                res.append("Pop")
                i += 1
            res.append("Push")
            i += 1
        return res
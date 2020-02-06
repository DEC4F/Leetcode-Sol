"""
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.
"""
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        """
        T(n) = nlogn + n + n = O(nlogn) -- presort
        S(n) = O(n) -- size of dict
        """
        items.sort(key=lambda x: (x[0], -x[1]))
        scores = collections.defaultdict(int)
        for i, item in enumerate(items):
            if not scores.get(item[0]):
                for j in range(5):
                    scores[item[0]] += items[i + j][1]
                scores[item[0]] //= 5
        res = []
        for k, v in scores.items():
            res.append([k, v])
        return res
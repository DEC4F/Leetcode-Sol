"""
Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.
"""
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        """
        T(n) = O(N + logF + TF)
        S(n) = O(TF + F)
        """
        mp = defaultdict(lambda: defaultdict(int))
        menu = set()
        for cust, tbl, food in orders:
            mp[tbl][food] += 1
            menu.add(food)
        menu = sorted(menu)
        res = [['Table'] + menu]
        for tbl, foods in sorted(mp.items(), key=lambda x: int(x[0])):
            res.append([tbl] + [str(foods[food]) for food in menu])
        return res
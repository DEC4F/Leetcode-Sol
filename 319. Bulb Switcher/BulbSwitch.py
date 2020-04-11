"""
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.
"""


class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        the kth bulb will be turned on by its factors-th operation
        so numbers with odd number of factors will stay on

        only number with perfect square as its factor will have odd number of factors, and thus stayed on
        """
        return int(math.sqrt(n))
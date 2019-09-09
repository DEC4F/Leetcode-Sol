"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:

    def climbStairs_dp_list(self, n: int) -> int:
        """
        T(n) = O(n) -- one pass
        S(n) = O(n) -- used a list to store subprob solution
        """
        if n == 1:
            return 1
        ans = [0]*(n+1)
        ans[1] = 1
        ans[2] = 2
        for i in range(3, n+1):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[-1]

    def climbStairs_dp_const(self, n: int) -> int:
        """
        T(n) = O(n) -- one pass
        S(n) = O(1) -- only used constant space to store previous sol
        """
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first, second = second, third
        return second

    def climbStairs_state_trans_mat(self, n: int) -> int:
        """
        T(n) = O(logn) -- approaching the solution from n/2
        S(n) = O(1) -- only stored the state transition matrix
        """
        import numpy as np
        mat = np.array([[1,1], [1,0]])
        return np.linalg.matrix_power(mat, n)[0,0]
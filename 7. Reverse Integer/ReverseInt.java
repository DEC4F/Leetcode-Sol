/**
 Given a 32-bit signed integer, reverse digits of an integer.
 */

class Solution {

    /**
       T(n) = O(n)
       S(n) = O(1)
     */
    public int reverse(int x) {
        int result = 0;
        while (x != 0) {
            int pop = x % 10;
            int newResult = result * 10 + pop;
            if ((newResult - pop)/10 != result)
                return 0;
            result = newResult;
            x /= 10;
        }
        return result;
    }
}

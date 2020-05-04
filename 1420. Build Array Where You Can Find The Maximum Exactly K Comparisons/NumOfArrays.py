"""
Given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers

---------------------------
max_val = -1
max_idx = -1
cost = 0
n = arr.length
for (i = 0; i < n; i++) {
    if max_val < arr[i] {
        max_val = arr[i]
        max_idx = i
        cost ++
    }
}
return max_idx
---------------------------

You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 10^9 + 7.
"""
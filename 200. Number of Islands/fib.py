def f1(n):
    if n == 0 or n == 1:
        return 1
    else:
        a = f1(n-1)
        b = f1(n-2)
        return a+b

def f2(n):
    fib = [1, 1]
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
    return fib[n]

def f3(n):
    if n == 0 or n == 1:
        return 1
    else:
        a = 1
        b = 1
        for i in range(2, n+1):
            c = a
            a = b
            b = a + c
        return b

def f4(n):
    import numpy as np
    mat = np.array([[1, 1], [1, 0]])
    return np.linalg.matrix_power(mat, n)[0, 0]

n = 100
#print(f1(n))
print("DP_1D: ", f2(n))
print("DP_Const: ", f3(n))
print("State_Mat: ", f4(n))
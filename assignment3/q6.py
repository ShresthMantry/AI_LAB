import numpy as np
import time


m = 106
n = 104


P = np.random.rand(m, n)
Q = np.random.rand(m, n)


start_time = time.time()
result_loop = np.zeros((m, m))
for i in range(m):
    for j in range(m):
        for k in range(n):
            result_loop[i, j] += P[i, k] * Q[j, k]  
end_time = time.time()
loop_time = end_time - start_time


start_time = time.time()
result_vec = np.dot(P, Q.T)
end_time = time.time()
vec_time = end_time - start_time


speedup = loop_time / vec_time

print("Matrix multiplication with Q transpose using loops:")
print(result_loop)

print("\nMatrix multiplication with Q transpose using vectorized operations:")
print(result_vec)

print("\nSpeedup:", speedup)

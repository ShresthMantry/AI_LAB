import numpy as np

equation_size = 3
A = np.random.rand(equation_size, equation_size)
b = np.random.rand(equation_size)
x = np.linalg.solve(A, b)
print("Coefficient Matrix A:")
print(A)

print("\nVector b:")
print(b)

print("\nSolution Vector x:")
print(x)

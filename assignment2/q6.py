import numpy as np

def transpose_and_flatten(matrix,n,m):
    transposed_matrix = np.empty((m,n),dtype=int)
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            transposed_matrix[i][j]=matrix[j][i]

    flattened_matrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            flattened_matrix.append(matrix[i][j])

    return transposed_matrix, flattened_matrix



n, m = map(int, input("Enter the number of rows and columns (N M): ").split())

matrix = []
print("Enter the matrix elements (space-separated):")
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

transposed_result, flattened_result = transpose_and_flatten(matrix,n,m)

print("\nTransposed Matrix:")
print(transposed_result)

print("\nFlattened Matrix:")
print(flattened_result)


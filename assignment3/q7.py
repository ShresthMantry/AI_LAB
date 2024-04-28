import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

second_column = arr[:, 1]
last_row = arr[-1, :]

print("Original 2D NumPy Array:")
print(arr)

print("\nExtracted Second Column:")
print(second_column)

print("\nExtracted Last Row:")
print(last_row)

import numpy as np

array_2d = np.array([[1, 2, 3, 4, 5, 6],
                     [4, 5, 6, 7, 8, 9],
                     [1, 2, 3, 4, 5, 6],
                     [7, 8, 9, 10, 11, 12],
                     [1, 2, 3, 4, 5, 6]])

flattened_array = array_2d.flatten()

unique_values, counts = np.unique(flattened_array, return_counts=True)

frequency_dict = dict(zip(unique_values, counts))

print("Original 2D Array:")
print(array_2d)

print("\nFrequency of Repeated Numbers:")
for num, freq in frequency_dict.items():
    print(f"Number {num}: {freq} times")

import numpy as np

array1 = np.random.rand(3, 4)
array2 = np.random.rand(3, 4)

concatenated_array = np.concatenate((array1, array2), axis=0)

sorted_array1 = np.sort(array1)
sorted_array2 = np.sort(array2)

sum_array = array1 + array2
difference_array = array1 - array2
product_array = array1 * array2
division_array = array1/array2

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\ni. Concatenated Array:")
print(concatenated_array)

print("\nii. Sorted Arrays:")
print("Sorted Array 1:")
print(sorted_array1)
print("Sorted Array 2:")
print(sorted_array2)

print("\niii. Sum of Arrays:")
print(sum_array)

print("\niv. Difference of Arrays:")
print(difference_array)

print("\nv. Product of Arrays:")
print(product_array)

print("\nvi. Division of Arrays:")
print(division_array)

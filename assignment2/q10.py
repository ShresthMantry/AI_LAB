import numpy as np

array_zeros = np.zeros(10)
array_ones = np.ones(10)
array_fives = np.full(10, 5)

array_even_integers = np.arange(10, 51, 2)

random_number = np.random.rand()

matrix = np.arange(1, 21).reshape(4, 5)

np.savetxt('matrix.txt', matrix)

loaded_matrix = np.loadtxt('matrix.txt')

print("i. Arrays of 10 zeros, 10 ones, 10 fives:")
print("Zeros:", array_zeros)
print("Ones:", array_ones)
print("Fives:", array_fives)

print("\nii. Array of even integers from 10 to 50:")
print("Even Integers:", array_even_integers)

print("\niii. Random Number between 0 and 1:")
print("Random Number:", random_number)

print("\niv. Original Matrix:")
print(matrix)

print("\nSaved Matrix (loaded from file):")
print(loaded_matrix)

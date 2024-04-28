import numpy as np

random_matrix = np.random.rand(8, 7)
print("Random Matrix:")
print(random_matrix)

max_values =  -100
min_value = 1000

for i in range(7):
    for j in range(8):
        max_values = max(max_values,random_matrix[j][i])
        min_value = min(min_value,random_matrix[j][i])
    print("Max and min of each column")
    print(max_values)
    print(min_value)







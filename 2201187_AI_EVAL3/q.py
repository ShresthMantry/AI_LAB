# 72 59 96 87 95 86 73 93 91 84

import random
import numpy as np


N = 10
k = 3


marks = list(map(int, input("Enter marks of 10 students separated by spaces: ").split()))


groups = [marks[i::k] for i in range(k)]

def objective_function(groups):
    return sum(np.std(group) for group in groups if len(group) > 1)


def get_neighbors(groups):
    neighbors = []
    for i in range(len(groups)):
        for j in range(len(groups)):
            if i != j and groups[i] and len(groups[i]) > 1:  # Ensure group[i] has at least two elements
                for student in groups[i]:
                    new_groups = [group[:] for group in groups]
                    new_groups[i].remove(student)
                    new_groups[j].append(student)
                    neighbors.append(new_groups)
    return neighbors


def stochastic_hill_climbing(groups, max_iterations=1000):
    current_value = objective_function(groups)
    iteration = 0
    while iteration < max_iterations:
        neighbors = get_neighbors(groups)
        next_groups, next_value = min((neighbor, objective_function(neighbor)) for neighbor in neighbors)
        if next_value < current_value or random.random() < np.exp(next_value - current_value):
            groups, current_value = next_groups, next_value
        else:
            break
        iteration += 1
    return groups

print("Initial groups:", marks)
final_groups = stochastic_hill_climbing(groups)


for i, group in enumerate(final_groups):
    print(f'Group {i+1}: {group}, Diversity: {np.std(group)}')
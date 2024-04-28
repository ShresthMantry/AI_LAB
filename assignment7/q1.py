import random

# Function to be maximized
def fitness_func(x):
    return 2 * x**2 + 1

# Initialize population
population_size = 100
population = [(random.uniform(0, 6), 0) for _ in range(population_size)]

# Evaluation of population
for i in range(population_size):
    population[i] = (population[i][0], fitness_func(population[i][0]))

# Genetic algorithm parameters
num_generations = 100
mutation_rate = 0.1
crossover_rate = 0.9

# Genetic algorithm
for generation in range(num_generations):
    # Selection
    new_population = []
    elite_size = int(population_size * 0.2)
    for _ in range(elite_size):
        best_idx = 0
        for i in range(1, population_size):
            if population[i][1] > population[best_idx][1]:
                best_idx = i
        new_population.append(population[best_idx])
        population[best_idx] = (-1, -float('inf'))

    # Crossover and mutation
    while len(new_population) < population_size:
        parent1_idx = random.randint(0, elite_size - 1)
        parent2_idx = random.randint(0, elite_size - 1)
        parent1 = new_population[parent1_idx]
        parent2 = new_population[parent2_idx]

        if random.random() < crossover_rate:
            child1 = random.uniform(min(parent1[0], parent2[0]), max(parent1[0], parent2[0]))
            child2 = random.uniform(min(parent1[0], parent2[0]), max(parent1[0], parent2[0]))
        else:
            child1 = parent1[0]
            child2 = parent2[0]

        if random.random() < mutation_rate:
            child1 = random.uniform(0, 6)
        if random.random() < mutation_rate:
            child2 = random.uniform(0, 6)

        new_population.append((child1, fitness_func(child1)))
        new_population.append((child2, fitness_func(child2)))

    population = new_population

# Find the best solution
best_solution = (0, -float('inf'))
for individual in population:
    if individual[1] > best_solution[1]:
        best_solution = individual

print(f"Best solution: x = {best_solution[0]}, f(x) = {best_solution[1]}")
import random
import numpy as np

# Define the function to be maximized
def f(x):
    return 2 * x**2 + 1

# Initialize population
def initialize_population(pop_size):
    return [random.uniform(0, 6) for _ in range(pop_size)]

# Define fitness function
def fitness(x):
    return f(x)

# Define selection function
def selection(population):
    tournament_size = 3
    return max(random.sample(population, tournament_size), key=fitness)

# Define crossover function
def crossover(parent1, parent2):
    alpha = random.random()
    return alpha * parent1 + (1 - alpha) * parent2

# Define mutation function
def mutation(individual):
    if random.random() < 0.1:  # mutation rate
        return random.uniform(0, 6)
    return individual

# Define GA function
def genetic_algorithm(population, generations):
    for _ in range(generations):
        new_population = []
        for _ in range(len(population)):
            parent1 = selection(population)
            parent2 = selection(population)
            offspring = crossover(parent1, parent2)
            offspring = mutation(offspring)
            new_population.append(offspring)
        population = new_population
    return max(population, key=fitness)

# Run GA
population = initialize_population(100)
best_solution = genetic_algorithm(population, 100)
print(f"Best solution: x = {best_solution}, f(x) = {f(best_solution)}")
import numpy as np
import random
import time

# Define the distance matrix (assuming symmetric TSP)
def create_distance_matrix(n):
    np.random.seed(42)
    return np.random.randint(1, 100, size=(n, n))
ˀ.ˀˀˀ
# Initialize population
def init_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population

# Calculate the total distance of a routeˀˀˀ
def total_distance(route, distance_matrix):
    dist = 0
    num_cities = len(route)
    for i in range(num_cities - 1):
        dist += distance_matrix[route[i]][route[i + 1]]
    dist += distance_matrix[route[-1]][route[0]]  # Return to starting city
    return dist

# Select parents for crossover
def selection(population, num_parents, distance_matrix):
    parents = []
    for _ in range(num_parents):
        selected = random.choice(population)
        parents.append(selected)
    parents.sort(key=lambda x: total_distance(x, distance_matrix))
    return parents[:2]

# Perform crossover to create offspring
def crossover(parent1, parent2):
    child = [-1] * len(parent1)
    start, end = sorted([random.randint(0, len(parent1) - 1) for _ in range(2)])
    child[start:end] = parent1[start:end]
    for idx, gene in enumerate(parent2):
        if gene not in child:
            for idx, element in enumerate(child):
                if element == -1:
                    child[idx] = gene
                    break
    return child

# Perform mutation
def mutation(individual, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

# Genetic algorithm
def genetic_algorithm(distance_matrix, pop_size=50, num_generations=100, mutation_rate=0.01):
    num_cities = len(distance_matrix)
    population = init_population(pop_size, num_cities)
    best_route = []
    best_distance = float('inf')
    
    start_time = time.time()
    for _ in range(num_generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = selection(population, 2, distance_matrix)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            new_population.extend([child1, child2])
        
        population = new_population
        for individual in population:
            dist = total_distance(individual, distance_matrix)
            if dist < best_distance:
                best_distance = dist
                best_route = individual
    
    end_time = time.time()
    computational_time = end_time - start_time
    
    return best_route, best_distance, computational_time

# Example usage
if __name__ == "__main__":
    num_cities = 10
    distance_matrix = create_distance_matrix(num_cities)
    best_route, best_distance, computational_time = genetic_algorithm(distance_matrix)
    print("Best route:", best_route)
    print("Best distance:", best_distance)
    print("Computational time:", computational_time, "seconds")

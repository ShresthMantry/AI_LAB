import random

# Constants
K = 3  # Number of groups
NUM_GENERATIONS = 100
POPULATION_SIZE = 50
CROSSOVER_PROB = 0.8
MUTATION_PROB = 0.2

# Sample data
marks = [random.randint(50, 100) for _ in range(100)]  # Random marks for 100 students

# Fitness function
def fitness(chromosome):
    group_sums = [0] * K
    group_counts = [0] * K
    for i, group in enumerate(chromosome):
        group_sums[group] += marks[i]
        group_counts[group] += 1
    group_means = [group_sum / count if count != 0 else 0 for group_sum, count in zip(group_sums, group_counts)]
    diversity = sum(sum((mark - group_means[group]) ** 2 for i, mark in enumerate(marks) if chromosome[i] == group)
                    for group in range(K))
    return 1 / (diversity + 1)

# Crossover function
def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation function
def swap_mutation(chromosome):
    index1 = random.randint(0, len(chromosome) - 1)
    index2 = random.randint(0, len(chromosome) - 1)
    chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]
    return chromosome

# Genetic algorithm
def genetic_algorithm():
    # Initialize population
    population = [[random.randint(0, K - 1) for _ in range(len(marks))] for _ in range(POPULATION_SIZE)]
    for _ in range(NUM_GENERATIONS):
        # Evaluate fitness
        fitnesses = [fitness(chromosome) for chromosome in population]
        # Select parents
        parents = random.choices(population, weights=fitnesses, k=POPULATION_SIZE)
        # Generate offspring
        offspring = []
        for i in range(0, POPULATION_SIZE, 2):
            parent1, parent2 = parents[i], parents[i + 1]
            # Crossover
            if random.random() < CROSSOVER_PROB:
                child1, child2 = single_point_crossover(parent1, parent2)
            else:
                child1, child2 = parent1[:], parent2[:]
            # Mutation
            if random.random() < MUTATION_PROB:
                child1 = swap_mutation(child1)
            if random.random() < MUTATION_PROB:
                child2 = swap_mutation(child2)
            offspring.extend([child1, child2])
        population = offspring
    # Return the best solution
    best_chromosome = max(population, key=fitness)
    return best_chromosome

# Run the genetic algorithm
best_chromosome = genetic_algorithm()
print("Best chromosome:", best_chromosome)
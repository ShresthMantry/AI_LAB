import random
from typing import List

# Define the number of students and groups
N = 100  # Number of students
K = 5    # Number of groups

# Generate random marks for students
marks = [random.randint(0, 100) for _ in range(N)]

# Define the population size and number of generations
POPULATION_SIZE = 100
NUM_GENERATIONS = 1000

# Define the tournament size for selection
TOURNAMENT_SIZE = 5

# Define the crossover and mutation probabilities
CROSSOVER_PROB = 0.8
MUTATION_PROB = 0.2

# Define the fitness function
def fitness(chromosome: List[int]) -> float:
    group_sums = [0] * K
    group_counts = [0] * K

    for i, group in enumerate(chromosome):
        group_sums[group] += marks[i]
        group_counts[group] += 1

    group_means = [group_sum / count if count != 0 else 0 for group_sum, count in zip(group_sums, group_counts)]

    diversity = sum(sum((mark - group_means[group]) ** 2 for i, mark in enumerate(marks) if chromosome[i] == group)
                    for group in range(K))

    return 1 / (diversity + 1)  # Maximize the fitness function

# Define the genetic algorithm
def genetic_algorithm(population: List[List[int]]) -> List[int]:
    for _ in range(NUM_GENERATIONS):
        # Evaluate the fitness of each chromosome in the population
        fitnesses = [fitness(chromosome) for chromosome in population]

        # Select parents for the next generation
        parents = [tournament_selection(population, fitnesses) for _ in range(POPULATION_SIZE)]

        # Create the next generation
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

# Helper functions
def tournament_selection(population: List[List[int]], fitnesses: List[float]) -> List[int]:
    tournament = random.sample(range(len(population)), TOURNAMENT_SIZE)
    best_idx = max(tournament, key=lambda i: fitnesses[i])
    return population[best_idx]

def single_point_crossover(parent1: List[int], parent2: List[int]) -> List[int]:
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def swap_mutation(chromosome: List[int]) -> List[int]:
    idx1, idx2 = random.sample(range(len(chromosome)), 2)
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

# Generate the initial population
population = [[random.randint(0, K - 1) for _ in range(N)] for _ in range(POPULATION_SIZE)]

# Run the genetic algorithm
best_chromosome = genetic_algorithm(population)

# Print the group assignments and diversity values
group_sums = [0] * K
group_counts = [0] * K

for i, group in enumerate(best_chromosome):
    group_sums[group] += marks[i]
    group_counts[group] += 1

group_means = [group_sum / count if count != 0 else 0 for group_sum, count in zip(group_sums, group_counts)]

diversity = sum(sum((mark - group_means[group]) ** 2 for i, mark in enumerate(marks) if best_chromosome[i] == group)
                for group in range(K))

print("Group assignments:")
for i, group in enumerate(best_chromosome):
    print(f"Student {i}: Group {group}")

print("\nDiversity values:")
for group in range(K):
    group_diversity = sum((mark - group_means[group]) ** 2 for i, mark in enumerate(marks) if best_chromosome[i] == group)
    print(f"Group {group}: {group_diversity:.2f}")

print(f"\nTotal diversity: {diversity:.2f}")
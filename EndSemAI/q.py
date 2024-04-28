import random
import math

# Parameters
n_queens = 8
population_size = 100
mutation_rate = 0.01
crossover_rate = 0.9
elitism_count = 1
temperature = 10000
cooling_rate = 0.003
maxFitness = 100

# Generate initial population
def generate_population(size):
    return [[random.uniform(0, 7) for _ in range(n_queens)] for _ in range(size)]

# Calculate fitness
def calculate_fitness(individual):
    horizontal_collisions = sum([individual.count(queen)-1 for queen in individual])/2
    diagonal_collisions = 0

    n = len(individual)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n
    for i in range(n):
        left_diagonal[i + round(individual[i]) - 1] += 1
        right_diagonal[len(individual) - i + round(individual[i]) - 2] += 1

    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))
    
    return int(maxFitness - (horizontal_collisions + diagonal_collisions))

# Selection
def selection(population):
    population = sorted(population, key=lambda x: calculate_fitness(x), reverse=True)
    return population[:elitism_count] + random.choices(population, k=len(population) - elitism_count)

# Crossover
def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        index1 = random.randint(0, len(parent1) - 1)
        index2 = random.randint(index1, len(parent1) - 1)
        child1 = parent1[:index1] + parent2[index1:index2] + parent1[index2:]
        child2 = parent2[:index1] + parent1[index1:index2] + parent2[index2:]
        return child1, child2
    else:
        return parent1, parent2

# Mutation
def mutation(individual):
    if random.random() < mutation_rate:
        index1 = random.randint(0, len(individual) - 1)
        index2 = random.randint(0, len(individual) - 1)
        individual[index1], individual[index2] = individual[index2], individual[index1]
    return individual

# Simulated Annealing
def simulated_annealing(individual,temperature):
    for _ in range(len(individual)):
        new_individual = list(individual)
        index1 = random.randint(0, len(new_individual) - 1)
        index2 = random.randint(0, len(new_individual) - 1)
        new_individual[index1], new_individual[index2] = new_individual[index2], new_individual[index1]
        
        old_fitness = calculate_fitness(individual)
        new_fitness = calculate_fitness(new_individual)
        fitness_difference = new_fitness - old_fitness
        
        if fitness_difference > 0 or random.random() < math.exp(fitness_difference / temperature):
            individual = new_individual
            
        temperature *= 1 - cooling_rate
    return individual

# Main function
def main():
    population = generate_population(population_size)
    
    for _ in range(1000):  # Maximum number of iterations
        population = selection(population)
        new_population = []
        
        for i in range(0, len(population), 2):
            parent1 = population[i]
            parent2 = population[i+1]
            child1, child2 = crossover(parent1, parent2)
            new_population += [mutation(child1), mutation(child2)]
        
        population = new_population
        
        for individual in population:
            individual = simulated_annealing(individual,1000)
        
        best_individual = max(population, key=lambda x: calculate_fitness(x))
        if calculate_fitness(best_individual) == maxFitness:
            print("Solution found:",  best_individual)
            break

if __name__ == "__main__":
    main()
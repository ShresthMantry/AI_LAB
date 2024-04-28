import random
import time

num_questions = 10
pop_size = 15
cross_prob = 0.6
mut_prob = 0.5
max_generations = 30

population = [[random.randint(0, 1) for _ in range(num_questions)] for _ in range(pop_size)]

def fitness(individual):
    return sum(individual)

def roulette_selection(population):
    fitness_values = [fitness(ind) for ind in population]
    total_fitness = sum(fitness_values)
    r = random.uniform(0, total_fitness)
    acc = 0
    for ind, fitness_value in zip(population, fitness_values):
        acc += fitness_value
        if acc >= r:
            return ind

def crossover(parent1, parent2):
    if random.random() < cross_prob:
        point1 = random.randint(1, num_questions - 2)
        point2 = random.randint(point1, num_questions - 1)
        child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
        child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
        return child1, child2
    else:
        return parent1, parent2

def mutate(individual):
    return [bit if random.random() > mut_prob else 1 - bit for bit in individual]

start_time = time.time()

for generation in range(max_generations):
    new_population = []
    for _ in range(pop_size // 2):
        parent1 = roulette_selection(population)
        parent2 = roulette_selection(population)
        child1, child2 = crossover(parent1, parent2)
        new_population.extend((mutate(child1), mutate(child2)))
    population = new_population


best_individual = max(population, key=fitness)
# print("Initial population: ", population)
print("Best individual: ", best_individual)
print("Fitness: ", fitness(best_individual))

end_time = time.time()
print("Computational time: ", end_time - start_time)
import random
import math
import time

# Function to calculate the diversity within a group
def calculate_diversity(group):
    diversity = 0
    group_mean = sum(group) / len(group)
    for mark in group:
        diversity += (mark - group_mean) ** 2
    return diversity

# Function to evaluate the fitness of a particle
def evaluate_fitness(particle, marks, k):
    groups = [[] for _ in range(k)]
    for i, student in enumerate(particle):
        groups[student].append(marks[i])

    total_diversity = 0
    for group in groups:
        if group:
            total_diversity += calculate_diversity(group)

    return total_diversity

# PSO implementation
def pso(marks, k, num_particles, max_iter, c1, c2, w):
    # Initialize particles and their velocities
    particles = [random.choices(range(k), k=len(marks)) for _ in range(num_particles)]
    velocities = [[0] * len(marks) for _ in range(num_particles)]

    # Initialize best positions and fitness values
    best_positions = particles.copy()
    best_fitness = [evaluate_fitness(particle, marks, k) for particle in particles]
    global_best_position = particles[best_fitness.index(min(best_fitness))]
    global_best_fitness = min(best_fitness)

    # Iterate until convergence or maximum iterations reached
    for _ in range(max_iter):
        for i in range(num_particles):
            # Update velocity and position
            for j in range(len(marks)):
                r1 = random.uniform(0, 1)
                r2 = random.uniform(0, 1)
                velocities[i][j] = (w * velocities[i][j] +
                                    c1 * r1 * (best_positions[i][j] - particles[i][j]) +
                                    c2 * r2 * (global_best_position[j] - particles[i][j]))
                particles[i][j] = (particles[i][j] + int(velocities[i][j])) % k

            # Evaluate fitness and update best positions
            fitness = evaluate_fitness(particles[i], marks, k)
            if fitness < best_fitness[i]:
                best_positions[i] = particles[i].copy()
                best_fitness[i] = fitness
            if fitness < global_best_fitness:
                global_best_position = particles[i].copy()
                global_best_fitness = fitness

    # Report group assignments and diversity values
    groups = [[] for _ in range(k)]
    for i, student in enumerate(global_best_position):
        groups[student].append(marks[i])

    print("Group assignments and diversity values:")
    for i, group in enumerate(groups):
        diversity = calculate_diversity(group)
        print(f"Group {i+1}: {group} (Diversity: {diversity:.2f})")

    return global_best_fitness

# Example usage
marks = [80, 75, 90, 85, 70, 95, 60, 85, 75, 80]  # Student marks
k = 3  # Number of groups
num_particles = 20
max_iter = 100
c1 = 2.0  # Cognitive constant
c2 = 2.0  # Social constant
w = 0.7  # Inertia weight

start_time = time.time()
best_fitness = pso(marks, k, num_particles, max_iter, c1, c2, w)
end_time = time.time()

print("\nPerformance metrics:")
print(f"Best fitness (minimum diversity): {best_fitness:.2f}")
print(f"Convergence rate: {max_iter} iterations")
print(f"Computational time: {end_time - start_time:.6f} seconds")
import numpy as np
import random
import math

# Function to calculate the total distance of a tour
def total_distance(tour, distances):
    total = 0
    num_cities = len(tour)
    for i in range(num_cities):
        total += distances[tour[i]][tour[(i + 1) % num_cities]]
    return total

# Simulated Annealing algorithm
def simulated_annealing(distances, initial_temperature, cooling_rate, num_iterations):
    num_cities = len(distances)
    current_tour = list(range(num_cities))
    random.shuffle(current_tour)
    current_distance = total_distance(current_tour, distances)

    best_tour = current_tour.copy()
    best_distance = current_distance

    temperature = initial_temperature

    for _ in range(num_iterations):
        new_tour = current_tour.copy()

        # Swap two random cities to get a new tour
        i, j = random.sample(range(num_cities), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

        new_distance = total_distance(new_tour, distances)

        # If the new tour is better, accept it
        if new_distance < current_distance:
            current_tour = new_tour
            current_distance = new_distance
            if current_distance < best_distance:
                best_tour = current_tour
                best_distance = current_distance
        else:
            # If the new tour is worse, accept it with a certain probability
            probability = math.exp((current_distance - new_distance) / temperature)
            if random.random() < probability:
                current_tour = new_tour
                current_distance = new_distance

        # Cool down the temperature
        temperature *= cooling_rate

    return best_tour, best_distance

# Example usage
# Define distances between cities (example)
cities = ['A', 'B', 'C', 'D']
distances = np.array([[0, 10, 15, 20],
                       [10, 0, 35, 25],
                       [15, 35, 0, 30],
                       [20, 25, 30, 0]])

# Experiment with different parameters
initial_temperature = 1000
cooling_rate = 0.99
num_iterations = 1000

best_tour, best_distance = simulated_annealing(distances, initial_temperature, cooling_rate, num_iterations)
print("Best tour:", best_tour)
print("Best distance:", best_distance)

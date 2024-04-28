import random

def f(x):
    return -(x ** 2)  

def hill_climbing(initial_x, step_size, range_min, range_max):
    current_x = initial_x
    while True:
        current_value = f(current_x)
        neighbors = [current_x + step_size, current_x - step_size]
        next_x = max(neighbors, key=lambda x: f(x))  
        if f(next_x) <= current_value:  
            break
        current_x = next_x
    return current_x, f(current_x)

initial_values = [-10, 0, 10]  
step_sizes = [0.1, 0.5, 1.0]  

for initial_value in initial_values:
    for step_size in step_sizes:
        max_x, max_value = hill_climbing(initial_value, step_size, -100, 100) 
        print(f"Initial Value: {initial_value}, Step Size: {step_size}, Maximum at x = {max_x}, f(x) = {max_value}")

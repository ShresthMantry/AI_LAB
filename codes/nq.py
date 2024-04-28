from queue import PriorityQueue

def is_valid(state):
    missionaries, cannibals, boat = state
    if missionaries < 0 or missionaries > 3 or \
       cannibals < 0 or cannibals > 3 or \
       (missionaries != 0 and missionaries < cannibals):
        return False
    if boat not in [0, 1]:
        return False
    return True

def is_goal(state):
    return state == (0, 0, 0)

def successors(state):
    successors = []
    missionaries, cannibals, boat = state
    if boat == 0:
        next_states = [(missionaries-i, cannibals-j, 1) for i in range(3) for j in range(3) if 1 <= i + j <= 2]
    else:
        next_states = [(missionaries+i, cannibals+j, 0) for i in range(3) for j in range(3) if 1 <= i + j <= 2]
    for next_state in next_states:
        if is_valid(next_state):
            successors.append(next_state)
    return successors

def uniform_cost_search():
    initial_state = (3, 3, 1)
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    came_from = {}
    cost_so_far = {}
    came_from[initial_state] = None
    cost_so_far[initial_state] = 0

    while not frontier.empty():
        _, current_state = frontier.get()
        if is_goal(current_state):
            return current_state

        for next_state in successors(current_state):
            new_cost = cost_so_far[current_state] + get_cost(current_state, next_state)
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = new_cost
                frontier.put((priority, next_state))
                came_from[next_state] = current_state

    return None

def get_cost(current_state, next_state):
    missionaries_diff = abs(current_state[0] - next_state[0])
    cannibals_diff = abs(current_state[1] - next_state[1])
    return missionaries_diff * 10 + cannibals_diff * 20

def print_solution(solution, came_from):
    path = []
    current_state = solution
    while current_state:
        path.append(current_state)
        current_state = came_from[current_state]
    path.reverse()

    for i, state in enumerate(path):
        print(f"Step {i}: ({state[0]}, {state[1]}, {state[2]})")

if __name__ == "__main__":
    solution = uniform_cost_search()
    if solution:
        print("Solution found:")
        print_solution(solution, came_from)
    else:
        print("No solution found.")

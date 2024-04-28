import heapq

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x_goal, y_goal = divmod(state[i][j] - 1, 3)
                distance += abs(i - x_goal) + abs(j - y_goal)
    return distance

def possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if i > 0:
                    moves.append((i, j, i - 1, j))
                if i < 2:
                    moves.append((i, j, i + 1, j))
                if j > 0:
                    moves.append((i, j, i, j - 1))
                if j < 2:
                    moves.append((i, j, i, j + 1))
    return moves

class State:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  
        self.h = h  

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def a_star_search(initial_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.state == goal_state:
            path = []
            while current_state:
                path.append(current_state.state)
                current_state = current_state.parent
            return path[::-1]

        closed_set.add(tuple(map(tuple, current_state.state)))

        for move in possible_moves(current_state.state):
            new_state = [row[:] for row in current_state.state]
            new_state[move[0]][move[1]], new_state[move[2]][move[3]] = new_state[move[2]][move[3]], new_state[move[0]][move[1]]

            if tuple(map(tuple, new_state)) not in closed_set:
                new_node = State(new_state, current_state, current_state.g + 1, heuristic(new_state))
                heapq.heappush(open_list, new_node)


def greedy_best_first_search(initial_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.state == goal_state:
            path = []
            while current_state:
                path.append(current_state.state)
                current_state = current_state.parent
            return path[::-1]

        closed_set.add(tuple(map(tuple, current_state.state)))

        for move in possible_moves(current_state.state):
            new_state = [row[:] for row in current_state.state]
            new_state[move[0]][move[1]], new_state[move[2]][move[3]] = new_state[move[2]][move[3]], new_state[move[0]][move[1]]

            if tuple(map(tuple, new_state)) not in closed_set:
                new_node = State(new_state, current_state, 0, heuristic(new_state))
                heapq.heappush(open_list, new_node)

initial_state = State([[1, 2, 3],
                       [4, 5, 6],
                       [0, 7, 8]])

print("A* Search:")
a_star_path = a_star_search(initial_state)
for step, state in enumerate(a_star_path):
    print("Step:", step)
    for row in state:
        print(row)
    print()

print("Greedy Best First Search:")
greedy_path = greedy_best_first_search(initial_state)
for step, state in enumerate(greedy_path):
    print("Step:", step)
    for row in state:
        print(row)
    print()

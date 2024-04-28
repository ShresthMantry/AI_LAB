from collections import deque
import heapq as hq

class State:
    def __init__(self, missionaries, cannibals, boat, cost):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.cost = cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __str__(self):
        return f"Missionaries: {self.missionaries}, Cannibals: {self.cannibals}, Boat: {self.boat}, Cost: {self.cost}"

    def is_valid(self):
        if self.missionaries < 0 or self.missionaries > 3 or self.cannibals < 0 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries != 0:
            return False
        if 3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries != 0:
            return False
        return True

    def successors(self):
        successors = []
        if self.boat == 'left':
            new_state = State(self.missionaries - 1, self.cannibals, 'right', self.cost + 10)
            if new_state.is_valid():
                successors.append(new_state)
            new_state = State(self.missionaries, self.cannibals - 1, 'right', self.cost + 20)
            if new_state.is_valid():
                successors.append(new_state)
            new_state = State(self.missionaries - 2, self.cannibals, 'right', self.cost + 20)
            if new_state.is_valid():
                successors.append(new_state)
            new_state = State(self.missionaries, self.cannibals - 2, 'right', self.cost + 40)
            if new_state.is_valid():
                successors.append(new_state)
            new_state = State(self.missionaries - 1, self.cannibals - 1, 'right', self.cost + 30)
            if new_state.is_valid():
                successors.append(new_state)
        else:
            new_state = State(self.missionaries + 1, self.cannibals, 'left', self.cost + 10)
            if new_state.is_valid():
                successors.append(new_state)
            new_state = State(self.missionaries, self.cannibals + 1, 'left', self.cost + 20)
            if new_state.is_valid():
                successors.append(new_state)
            new_state = State(self.missionaries + 2, self.cannibals, 'left', self.cost + 20)
            if new_state.is_valid():
                successors.append(new_state)
            new_state = State(self.missionaries, self.cannibals + 2, 'left', self.cost + 40)
            if new_state.is_valid():
                successors.append(new_state)
            new_state = State(self.missionaries + 1, self.cannibals + 1, 'left', self.cost + 30)
            if new_state.is_valid():
                successors.append(new_state)
        return successors

def bfs():
    initial_state = State(3, 3, 'left', 0)
    visited = set()
    # queue = deque([initial_state])
    ol = []
    hq.heappush(ol,initial_state)


    while ol:
        state = hq.heappop(ol)
        if state not in visited:
            visited.add(state)
            if state.missionaries == 0 and state.cannibals == 0 and state.boat == 'right':
                return state
            for successor in state.successors():
                if successor not in visited:
                    hq.heappush(ol,successor)
    return None

def main():
    solution = bfs()
    if solution:
        print("Solution found:")
        print(solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

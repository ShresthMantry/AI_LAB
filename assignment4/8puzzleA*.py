from collections import deque
import heapq as h

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x_goal, y_goal = divmod(state[i][j] - 1, 3)
                distance += abs(i - x_goal) + abs(j - y_goal)
    return distance

def print_state(state):
    for row in state:
        for column in row :
            print(column,end=" ")
        print()

def possible_actions(state):
    actions = []
    pos = none_pos(state)

    if pos[0] > 0:
        actions.append('up')
    if pos[0] < 2:
        actions.append('down')
    if pos[1] > 0:
        actions.append('left')
    if pos[1] < 2:
        actions.append('right')

    return actions

def none_pos(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return [i, j]

def apply_action(state, action):
    pos = none_pos(state)
    new = [row[:] for row in state]

    i, j = pos

    if action == 'up':
        new[i][j], new[i - 1][j] = new[i - 1][j], 0
    elif action == 'down':
        new[i][j], new[i + 1][j] = new[i + 1][j], 0
    elif action == 'left':
        new[i][j], new[i][j - 1] = new[i][j - 1], 0
    elif action == 'right':
        new[i][j], new[i][j + 1] = new[i][j + 1], 0

    return new

def bfs(initial, goal):
    open_list = []
    h.heappush(open_list,(0,initial,[]))
    closed_list = []

    while open_list:
        level,state,path =h.heappop(open_list)
        
        if state == goal:
            return path

        closed_list.append(state)

        for action in possible_actions(state):
            successor_state = apply_action(state, action)

            if successor_state not in closed_list:
                h.heappush(open_list,(heuristic(successor_state)+len(path),successor_state,path+[action]))

    return "Goal not reachable"


init_state = [
    [3, 8, 1],
    [6, 2, 5],
    [4, 7, 0]
]

goal_state = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]





sol_path = bfs(init_state, goal_state)

if sol_path != "Goal not reachable":
    print("Solution Path:")
    step = 1
    for action in sol_path:
        print("Step: ",step, " Move:  ",action)
        step += 1
else:
    print("Goal not reachable")
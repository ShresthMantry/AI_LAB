vj vjj 'def print_state(state):
    for row in state:
        for column in row:
            print(column, end=" ")
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
            if state[i][j] is None:
                return [i, j]

def apply_action(state, action):
    pos = none_pos(state)
    new = [row[:] for row in state]

    i, j = pos

    if action == 'up':
        new[i][j], new[i - 1][j] = new[i - 1][j], None
    elif action == 'down':
        new[i][j], new[i + 1][j] = new[i + 1][j], None
    elif action == 'left':
        new[i][j], new[i][j - 1] = new[i][j - 1], None
    elif action == 'right':
        new[i][j], new[i][j + 1] = new[i][j + 1], None

    return new

def dfs(initial, goal, path=[]):
    print("Current State:")
    print_state(initial)
    
    if initial == goal:
        return path
    
    for action in possible_actions(initial):
        successor_state = apply_action(initial, action)
        
        if successor_state not in path:
            new_path = dfs(successor_state, goal, path + [successor_state])
            if new_path:
                return new_path
    
    return None

init_state = [
    [3, 8, 1],
    [6, 2, 5],
    [4, 7, None]
]

goal_state = [
    [3, 8, 1],
    [6, 2, None],
    [4, 7, 5]
]

sol_path = dfs(init_state, goal_state)

if sol_path:
    print("Solution Path:")
    step = 1
    for state in sol_path:
        print("Step:", step)
        print_state(state)
        print()
        step += 1
else:
    print("Goal not reachable")
'
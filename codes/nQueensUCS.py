from collections import deque

def is_safe(board, row, col, N):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check lower diagonal on left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    return True

def solve_n_queens_bfs(N):
    solutions = []
    queue = deque()
    queue.append(([], 0))  # Initial state: empty board, 0 queens placed
    
    while queue:
        board, col = queue.popleft()
        
        if col == N:
            solutions.append(board)
            continue
        
        for i in range(N):
            if is_safe(board, i, col, N):
                new_board = [row[:] for row in board]
                new_board.append([1 if j == i else 0 for j in range(N)])
                queue.append((new_board, col + 1))
    
    return solutions

def print_board(board):
    for row in board:
        row_str = ""
        for val in row:
            row_str += str(val) + " "
        print(row_str.strip())
    print()

# Example usage:
N = 8
solutions = solve_n_queens_bfs(N)
if solutions:
    print(f"Total solutions for {N}-Queens problem: {len(solutions)}")
    for sol_idx, sol in enumerate(solutions, start=1):
        print(f"Solution {sol_idx}:")
        print_board(sol)
else:
    print(f"No solution exists for {N}-Queens problem.")

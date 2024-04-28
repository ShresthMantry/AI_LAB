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

def solve_n_queens_util(board, col, N, result):
    if col == N:
        result.append([row[:] for row in board])
        return True
    
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, N, result) or res
            board[i][col] = 0 # Backtrack if the queen can't be placed here
            
    return res

def solve_n_queens(N):
    result = []
    board = [[0]*N for _ in range(N)]
    
    if not solve_n_queens_util(board, 0, N, result):
        return None
    
    return result

def print_board(board):
    for row in board:
        row_str = ""
        for val in row:
            row_str += str(val) + " "
        print(row_str.strip())
    print()

# Example usage:
N = 8
solutions = solve_n_queens(N)
if solutions:
    print(f"Total solutions for {N}-Queens problem: {len(solutions)}")
    for sol_idx, sol in enumerate(solutions, start=1):
        print(f"Solution {sol_idx}:")
        print_board(sol)
else:
    print(f"No solution exists for {N}-Queens problem.")

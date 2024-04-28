def isSafe1(row, col, board, n):
    # Check upper element
    duprow, dupcol = row, col

    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    col, row = dupcol, duprow
    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1

    row, col = duprow, dupcol
    while row < n and col >= 0:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1

    return True

def heuristic(board, n):
    attacks = 0
    for col in range(n):
        for row in range(n):
            if board[row][col] == 'Q':
                attacks += count_attacks(row, col, board, n)
    return attacks

def count_attacks(row, col, board, n):
    attacks = 0
    for i in range(n):
        if board[i][col] == 'Q' and i != row:
            attacks += 1
        if board[row][i] == 'Q' and i != col:
            attacks += 1
        if 0 <= row + i < n and 0 <= col + i < n and board[row + i][col + i] == 'Q' and i != 0:
            attacks += 1
        if 0 <= row - i < n and 0 <= col + i < n and board[row - i][col + i] == 'Q' and i != 0:
            attacks += 1
    return attacks

def solveNQueensGBFS(n):
    ans = []
    stack = [(0, ['.' * n for _ in range(n)])]

    while stack:
        col, current_board = stack.pop()

        if col == n:
            ans.append(list(current_board))
            continue

        for row in range(n):
            if isSafe1(row, col, current_board, n):
                new_board = current_board.copy()
                new_board[row] = new_board[row][:col] + 'Q' + new_board[row][col + 1:]
                stack.append((col + 1, new_board))

        stack.sort(key=lambda x: heuristic(x[1], n))

    return ans

n = 8
ans = solveNQueensGBFS(n)
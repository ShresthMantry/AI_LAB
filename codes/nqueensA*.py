from queue import PriorityQueue

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

def solveNQueensAStar(n):
    ans = []
    open_list = PriorityQueue()
    open_list.put((heuristic(['.' * n for _ in range(n)], n), 0, ['.' * n for _ in range(n)]))

    while not open_list.empty():
        _, col, current_board = open_list.get()

        if col == n:
            ans.append(list(current_board))
            continue

        for row in range(n):
            if isSafe1(row, col, current_board, n):
                new_board = current_board.copy()
                new_board[row] = new_board[row][:col] + 'Q' + new_board[row][col + 1:]
                cost = col + 1
                priority = cost + heuristic(new_board, n)
                open_list.put((priority, col + 1, new_board))

    return ans

n = 8
ans = solveNQueensAStar(n)

for i in range(len(ans)):
    print(f"Arrangement {i + 1}")
    for j in range(len(ans[0])):
        print(ans[i][j])
    print()
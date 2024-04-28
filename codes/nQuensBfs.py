from queue import Queue

def isSafe1(row, col, board, n):
    # check upper element
    duprow = row
    dupcol = col

    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    col = dupcol
    row = duprow
    while col >= 0:
        if board[row][col] == 'Q':
            return False
        col -= 1

    row = duprow
    col = dupcol
    while row < n and col >= 0:
        if board[row][col] == 'Q':
            return False
        row += 1
        col -= 1

    return True

def solveNQueensBFS(n):
    ans = []
    queue = Queue()
    queue.put((0, ['.' * n for _ in range(n)]))

    while not queue.empty():
        col, current_board = queue.get()

        if col == n:
            ans.append(list(current_board))
            continue

        for row in range(n):
            if isSafe1(row, col, current_board, n):
                new_board = current_board.copy()
                new_board[row] = new_board[row][:col] + 'Q' + new_board[row][col + 1:]
                queue.put((col + 1, new_board))

    return ans

n = 8
ans = solveNQueensBFS(n)

for i in range(len(ans)):
    print(f"Arrangement {i + 1}")
    for j in range(len(ans[0])):
        print(ans[i][j])
    print()


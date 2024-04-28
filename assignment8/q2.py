import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))  # 0 represents empty, 1 represents X, -1 represents O
        self.player = 1  # Start with player X
        self.winning_positions = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                                  [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                                  [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

    def print_board(self):
        for row in self.board:
            print("|".join(["X" if cell == 1 else "O" if cell == -1 else " " for cell in row]))
            print("-----")
        print("\n")

    def is_winner(self, player):
        for positions in self.winning_positions:
            if all(self.board[pos] == player for pos in positions):
                return True
        return False

    def is_full(self):
        return not any(0 in row for row in self.board)

    def is_game_over(self):
        return self.is_winner(1) or self.is_winner(-1) or self.is_full()

    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.player
            self.player *= -1  # Switch player
            return True
        return False

    def evaluate(self):
        if self.is_winner(1):
            return 1
        elif self.is_winner(-1):
            return -1
        else:
            return 0

    def minimax(self, depth, maximizing_player, alpha, beta):
        if self.is_winner(1):
            return 1
        elif self.is_winner(-1):
            return -1
        elif self.is_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == 0:
                        self.board[i][j] = 1
                        eval = self.minimax(depth + 1, False, alpha, beta)
                        self.board[i][j] = 0
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == 0:
                        self.board[i][j] = -1
                        eval = self.minimax(depth + 1, True, alpha, beta)
                        self.board[i][j] = 0
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def find_best_move(self):
        best_move = None
        best_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.board[i][j] = 1
                    eval = self.minimax(0, False, float('-inf'), float('inf'))
                    self.board[i][j] = 0
                    if eval > best_eval:
                        best_eval = eval
                        best_move = (i, j)
        return best_move


if __name__ == "__main__":
    game = TicTacToe()
    while not game.is_game_over():
        game.print_board()
        if game.player == 1:
            row, col = game.find_best_move()
            game.make_move(row, col)
            print("AI (X) makes move: ", row, col)
        else:
            row, col = map(int, input("Enter your move (row col): ").split())
            while not game.make_move(row, col):
                print("Invalid move. Try again.")
                row, col = map(int, input("Enter your move (row col): ").split())
        print("\n")
    game.print_board()
    if game.is_winner(1):
        print("AI (X) wins!")
    elif game.is_winner(-1):
        print("You win!")
    else:
        print("It's a draw!")
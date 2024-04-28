import random

def alpha_beta_pruning(n, alpha, beta, maximizing_player):
    if n == 0:
        return 1 if maximizing_player else -1
    if n == 1:
        return -1 if maximizing_player else 1

    if maximizing_player:
        max_eval = float('-inf')
        for move in [1, 2]:
            if n - move >= 0:
                eval = alpha_beta_pruning(n - move, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for move in [1, 2]:
            if n - move >= 0:
                eval = alpha_beta_pruning(n - move, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def get_best_move(n):
    best_move = 1
    best_eval = float('-inf')
    for move in [1, 2]:
        if n - move >= 0:
            eval = alpha_beta_pruning(n - move, float('-inf'), float('inf'), True)
            if eval > best_eval:
                best_eval = eval
                best_move = move
    return best_move

n_stones = 50
first_player = random.choice([1, 2])
print(f"First player: Player {first_player}")

while n_stones > 0:
    print(f"\nStones left: {n_stones}")
    if first_player == 1:
        human_move = int(input("Human move (1 or 2): "))
        n_stones -= human_move
        if n_stones <= 0:
            print("Human wins!")
        else:
            first_player = 2
    else:
        ai_move = get_best_move(n_stones)
        print(f"AI move: {ai_move}")
        n_stones -= ai_move
        if n_stones <= 0:
            print("AI wins!")
        else:
            first_player = 1
import math

# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(0, 9, 3):
        print(f'{board[i]} | {board[i+1]} | {board[i+2]}')
        if i < 6:
            print('---------')

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Minimax function with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

# Function to get the best move for the AI
def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Main game loop
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Human player's turn
        while True:
            move = input("Enter your move (0-8): ")
            if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == ' ':
                board[int(move)] = 'X'
                break
            else:
                print("Invalid move. Try again.")

        print_board()

        if check_win(board, 'X'):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # AI player's turn
        print("AI is making a move...")
        ai_move = get_best_move(board)
        board[ai_move] = 'O'

        print_board()

        if check_win(board, 'O'):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

# Start the game
play_game()
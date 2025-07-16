import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in zip(*board):
        if all(cell == player for cell in col):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                moves.append((i, j))
    return moves

board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

current_player = "X"

while True:
    print_board(board)

    if current_player == "X":
        move = input("Player X, enter your move (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Try again.")
            continue

        row = (int(move) - 1) // 3
        col = (int(move) - 1) % 3

        if board[row][col] in ['X', 'O']:
            print("Cell already taken. Try another one.")
            continue
    else:
        print("Computer is making a move...")
        available_moves = get_available_moves(board)
        row, col = random.choice(available_moves)

    board[row][col] = current_player

    if check_winner(board, current_player):
        print_board(board)
        print(f"🎉 Player {current_player} wins!")
        break

    if is_full(board):
        print_board(board)
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"

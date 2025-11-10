import math

# board with empty spaces
board = [" " for _ in range(9)]

# print board
def print_board():
    for i in range(0, 9, 3):
        print(board[i], board[i+1], board[i+2])
    print()

# check winner
def winner(b, player):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    for s in win_states:
        if b[s[0]] == b[s[1]] == b[s[2]] == player:
            return True
    return False

# check tie
def tie(b):
    return " " not in b

# minimax function
def minimax(b, isMax):
    if winner(b, "O"):
        return 1
    if winner(b, "X"):
        return -1
    if tie(b):
        return 0

    if isMax:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best

# AI move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# player move
def player_move():
    while True:
        pos = int(input("Enter your move (1-9): ")) - 1
        if 0 <= pos <= 8 and board[pos] == " ":
            board[pos] = "X"
            break
        else:
            print("Invalid move, try again.")

# main game loop
print("You are X, AI is O\n")
print_board()

while True:
    player_move()
    print_board()
    if winner(board, "X"):
        print("You win!")
        break
    if tie(board):
        print("Draw!")
        break

    ai_move()
    print_board()
    if winner(board, "O"):
        print("AI wins!")
        break
    if tie(board):
        print("Draw!")
        break

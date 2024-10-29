def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    #check rows, columns, and diagonals
    for row in range(3):
        if all([spot == player for spot in board[row]]):
            return True
        for col in range(3):
            if all([board[row][col] == player for row in range(3)]):
                return True
        if all([board[row][col] == player for row in range (3)]):
            return True
        if all ([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
            return True
        return False
def is_board_full(board):
    return all([spot != " " for row in board for spot in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"player {players[current_player]}, enter the row (0, 1, or 2):"))
        col = int(input(f"player {players[current_player]}, enter the column (0, 1, or 2):"))

        if board[row][col] == " ":
            board[row][col] = players[current_player]
        else:
            print("The spot is already taken, try again.")
            continue

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"player {players[current_player]} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("The game is a tie!")
            break

        current_player = 1 - current_player 

        if __name__ == "__main__":
            tic_tac_toe()

            
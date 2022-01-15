# board
board = [
    "_", "_", "_",
    "_", "_", "_",
    "_", "_", "_"
]

game_is_active = True
winner = None
current_player = "X"

# display_board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# play_game
def play_game():
    display_board()

    # Loops game until winner
    while game_is_active:
        turn_handler(current_player)
        check_game_over()
        flip_player()

    # Displays a scenario when check_game_over() has identified a game over scenario
    if winner == "X" or winner == "O":
        print(winner, " won!")
    elif winner == None:
        print("Tie.")
    else:
        print("Unknown outcome has occurred.")


# turn_handler
def turn_handler(player_turn):
    print(player_turn, "'s turn\n")
    position = input("Choose a position from 1-9:\n")

    valid_input = False
    while not valid_input:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Please try again and input a position from 1-9:\n")

        position = int(position) - 1

        if board[position] == "_":
            valid_input = True
        else:
            print("That position is already used.")

    board[position] = player_turn
    display_board()


def flip_player():
    global current_player
    if current_player.upper() == "X":
        current_player = "O"
    elif current_player.upper() == "O":
        current_player = "X"
    return


def check_game_over():
    check_win()
    check_tie()
    return


# check_win scenarios (row, column, diagonal)
def check_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_is_active
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    if row1 or row2 or row3:
        game_is_active = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return


def check_columns():
    global game_is_active
    column1 = board[0] == board[3] == board[6] != "_"
    column2 = board[1] == board[4] == board[7] != "_"
    column3 = board[2] == board[5] == board[8] != "_"
    if column1 or column2 or column3:
        game_is_active = False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    return


def check_diagonals():
    global game_is_active
    diagonal1 = board[0] == board[4] == board[8] != "_"
    diagonal2 = board[2] == board[4] == board[6] != "_"
    if diagonal1 or diagonal2:
        game_is_active = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    return


# check_tie
def check_tie():
    global game_is_active
    if "_" not in board:
        game_is_active = False
        return True
    else:
        return False



play_game()

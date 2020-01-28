# creating the board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


#setting the game to true and winner will be none when the game starts
game_is_on = True
winner = None

#setting the players and taking their names
print('Player one will be X and player two will be O ')
player_one = input('Player one enter your name: ')
player_two = input('Player two enter your name: ')

#setting the current player to player one that is X
current_player = player_one

def play_game():
    # display initial board
    display_board()
    while game_is_on:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == player_one or winner == player_two:
        print(winner + " Won! ")
    elif winner == None:
        print("Tie")

#handle the players
def handle_turn(player):
    print(player + "'s turn")
    position = input('Enter a position from 1 - 9 ')
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input('Enter a position from 1 - 9 ')
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print('You cant go there')
    if player == player_one:
        board[position] = 'X'
    else:
        board[position] = 'O'
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_row():
    global game_is_on
    row_one = board[0] == board[1] == board[2] != "-"
    row_two = board[3] == board[4] == board[5] != "-"
    row_three = board[6] == board[7] == board[8] != "-"
    if row_one or row_two or row_three:
        game_is_on = False
    if row_one:
        return board[0]
    elif row_two:
        return board[3]
    elif row_three:
        return board[6]
    return

def check_column():
    global game_is_on
    column_one = board[0] == board[3] == board[6] != "-"
    column_two = board[1] == board[4] == board[7] != "-"
    column_three = board[2] == board[5] == board[8] != "-"
    if column_one or column_two or column_three:
        game_is_on = False
    if column_one:
        return board[0]
    elif column_two:
        return board[1]
    elif column_three:
        return board[2]
    return
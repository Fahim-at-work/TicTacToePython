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

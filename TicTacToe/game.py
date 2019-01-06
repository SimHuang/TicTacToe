game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
play_one_turn = True

def start_game():
    global  play_one_turn
    is_game_complete = False
    print("First Player is X. Second player is 0")

    while True:
        show_game_board()
        player_one_move = input("PlayerOne: Enter a number to select a move")
        set_player_move(player_one_move)
        show_game_board()
        play_one_turn = False

        status = get_game_status()
        if status != None :
            print(determine_winner(status))
            break;


        player_two_move = input("PlayerTwo: Enter a number to select a move")
        set_player_move(player_two_move)
        show_game_board()

        status = get_game_status()
        if status != None:
            print(determine_winner(status))
            break;


        #determine game finish
        play_one_turn = True


def show_game_board():
    for row in game_board:
        for location in row:
            print("{} | ".format(location), end='')
        print("\n")

def set_player_move(player_move):
    for row_index,row in enumerate(game_board):
        for loc_index,location in enumerate(row):
            if location == int(player_move):
                if play_one_turn:
                    game_board[row_index][loc_index] = "X"
                else:
                    game_board[row_index][loc_index] = "O"

def determine_winner(status):
    if status == 'TIE':
        return 'This Game is a tie!'
    elif status == 'O':
        return 'Player Two won!'
    elif status == 'X':
        return 'Player One Won!'


def get_game_status():
    is_tie = True
    winning_play = None
    #check that all columns and rows are filled
    for i_row,row in enumerate(game_board):
        for i_location, location in enumerate(row):
            if game_board[i_row][i_location] != "X" and game_board[i_row][i_location] != "0":
                is_tie = False
                break

    if is_tie:
        return "TIE"

    #check for winner
    if game_board[0][0] == game_board[1][0] and game_board[1][0] == game_board[2][0]:
        winning_play = game_board[0][0]
    elif game_board[0][0] == game_board[0][1] and game_board[0][1] == game_board[0][2]:
        winning_play = game_board[0][0]
    elif game_board[0][0] == game_board[1][1] and game_board[0][1] == game_board[2][2]:
        winning_play = game_board[0][0]
    elif game_board[0][1] == game_board[1][1] and game_board[1][1] == game_board[2][1]:
        winning_play = game_board[0][1]
    elif game_board[1][0] == game_board[1][1] and game_board[1][1] == game_board[1][2]:
        winning_play = game_board[1][0]

    return winning_play

start_game()

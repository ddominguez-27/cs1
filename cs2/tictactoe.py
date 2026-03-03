




#base_board = [['E','Ε','E'],['Ε','Е','Ε'],['E','Ε','E']] while all the characters look like e (E) there are 3 variations to avoid a line full of empty plots triggering the win detection function
#the character in the middle of the board is the crylic character  ye (Е) the characters on the edge of the board are the greek letter Epsilon (Ε)



def print_board(board):
    print(f"""

   1   2   3
1  {board[0][0]} | {board[0][1]} | {board[0][2]}
  ———————————
2  {board[1][0]} | {board[1][1]} | {board[1][2]}
  ———————————
3  {board[2][0]} | {board[2][1]} | {board[2][2]}

""")


def choose_players():
    while True:
        player1 = input("Would you like to play as 'X's or 'O's? (1 for X :: 2 for O)")
        if player1 == "1":
            player1 = 'X'
            player2 = 'O'
            print("""Player 1 has selected 'X'
Player 2 has automatically been assigned 'O'""")
            break
        elif player1 == "2":
            player1 = "O"
            player2 = 'X'
            print("""Player 1 has selected 'O'
Player 2 has automatically been assigned 'X'""")
            break
        else: 
            print("Please select either 1 or 2 to select character")
    return(player1, player2)
 

def player_move(player, board):
    while True:
        print_board(board)
        move = input(f"Player {player}'s Turn. Please select a grid space to move to as an ordered pair of row, collum (ie   1, 3   or   2, 2)")
        characters = list(move)
        counter = 0
        rowpos = -1
        columnpos = -1
        for i in characters:
            if i in ["1", "2", "3"]:
                if counter == 0:
                    rowpos = int(i) - 1
                    counter += 1
                elif counter == 1:
                    columnpos = int(i) - 1
                    counter += 1
                else:
                    pass
            else:
                pass
        if -1 in [rowpos, columnpos]:
            print("Invalid syntax. Please try again")
        elif board[rowpos][columnpos] in ['E','Е','Ε']:
            print(f"Row {rowpos+1}, Column {columnpos+1} selected")
            board[rowpos][columnpos] = player
            return(board)
        else:
            print("That space is taken, select a different space")
            


def check_win(board):

    #list of win conditions
    if 1 in [
    len(set([board[0][0], board[0][1], board[0][2]])),
    len(set([board[1][0], board[1][1], board[1][2]])),
    len(set([board[2][0], board[2][1], board[2][2]])),
    len(set([board[0][0], board[1][0], board[2][0]])),
    len(set([board[0][1], board[1][1], board[2][1]])),
    len(set([board[0][2], board[1][2], board[2][2]])),
    len(set([board[0][0], board[1][1], board[2][2]])),
    len(set([board[2][0], board[1][1], board[0][2]])),
    ]:
        return True
    else: 
        return False


def play_game():
    player1, player2 = choose_players()
    board = [['E','Ε','E'],['Ε','Е','Ε'],['E','Ε','E']]
    for i in range(9):
        if i % 2 == 0:
            board = player_move(player1, board)
            if check_win(board):
                print_board(board)
                print("Player 1 wins!")
                return
        else:
            board = player_move(player2, board)
            if check_win(board):
                print_board(board)
                print("Player 2 wins!")
                return 
    print_board(board)
    print("Its a draw!")


play_game()
play_game()

            

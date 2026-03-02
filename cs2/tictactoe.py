




base_board = [['E','Ε','E'],['Ε','Е','Ε'],['E','Ε','E']] #while all the characters look like e (E) there are 3 variations to avoid a line full of empty plots triggering the win detection function
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

board = [['E','E','E'],['E','E','E'],['E','E','E']]

print_board(board)

def choose_players():
    while True:
        player1 = input("Would you like to play as 'X's or 'O's? (1 for X :: 2 for O)")
        if player1 == "1":
            player1 = 'X'
            print("""Player 1 has selected 'X'
Player 2 has automatically been assigned 'O'""")
            break
        elif player1 == "2":
            player1 = "2"
            print("""Player 1 has selected 'O'
Player 2 has automatically been assigned 'X'""")
            break
        else: 
            print("Please select either 1 or 2 to select character")
 

def player_move(player):
    while True:
        move = input(f"{player}'s Turn. Please select a grid space to move to as a coordinate point (ie 1, 3   or 2, 2)")
        characters = list(move)
        counter = 0
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
        
        print(rowpos, columnpos)



def check_win(board):
    
    base_board = [['E','Ε','E'],['Ε','Е','Ε'],['E','Ε','E']]
    board = base_board
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
        print("a winner has been found")
    else: 
        pass
    
player_move("Player 1")
base_board = [['E','Ε','E'],['Ε','Е','Ε'],['E','Ε','E']]
check_win(base_board)
echeck = input("please input E")
if echeck == "E":
    print("thats an e (E)")
elif echeck == "Ε":
    print("Epsilon")
elif echeck == "Е":
    print("crylic")
choose_players()

base_board = [['E','Ε','E'],['Ε','Е','Ε'],['E','Ε','E']] #while all the characters look like e (E) there are 3 variations to avoid a line full of empty plots triggering the win detection function
#the character in the middle of the board is the crylic character  ye (Е) the characters on the edge of the board are the greek letter Epsilon (Ε)




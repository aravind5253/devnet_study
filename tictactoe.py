#----------------global variables---------
#board
board=["_","_","_","_","_","_","_","_","_"]
#If game is going
game_is_still_going=True
#Who won? or tie
Winner=None
#whos turn

current_player='X'


#display the board
def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

#play a game 
def play_game():
    #display board
    display_board()

    while game_is_still_going:

        #handle a single turn
        handle_turn(current_player)
        #check if game has ended
        check_if_game_over()
        #flip the player
        flip_player()
    

    #game has ended
    if Winner =='X'or Winner=='O':
        print(Winner + ' Won.')
    elif Winner == None:
        print("Tie")



    
#handle the turn
def handle_turn(player):
    print(player +"'s turn.")
    position=input("Choose a position from 1 to 9:")
    valid=False
    while not valid:


    
        while position not in ['1','2','3','4','5','6','7','8','9']:
         position=input("Choose a position from 1 to 9:")

        position=int(position)-1


        if board[position] =="_":
            valid=True
        else:
            print("Invalid place")

    board[position]=player


    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
   

    global Winner
    

    row_winner=check_rows()

    column_winner=check_columns()

    diagonal_winner=check_diagonal()

    if row_winner:
        Winner=row_winner
    
    elif column_winner:
        Winner=column_winner
    

    elif diagonal_winner:
        Winner=diagonal_winner
    
    else:
        Winner=None

        



    return


def check_rows():
    

    global game_is_still_going

    row_1= board[0]==board[1]==board[2]!="_"
    row_2= board[3]==board[4]==board[5]!="_"
    row_3= board[6]==board[7]==board[8]!="_"

    if row_1 or row_2 or row_3:
        game_is_still_going=False
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return


    

def check_columns():
    global game_is_still_going

    column_1= board[0]==board[3]==board[6]!="_"
    column_2= board[1]==board[4]==board[7]!="_"
    column_3= board[2]==board[5]==board[8]!="_"

    if column_1 or column_2 or column_3:
        game_is_still_going=False
    
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return

def check_diagonal():
    global game_is_still_going

    diagonal_1= board[0]==board[4]==board[8] != "_"
    diagonal_2= board[2]==board[4]==board[6] != "_"
    

    if diagonal_1 or diagonal_2:
        game_is_still_going=False   

    if diagonal_1:
        return board[0]

    elif diagonal_2:
        return board[2]
    
    return


def check_if_tie():
    global game_is_still_going
    if "_" not in board:
        game_is_still_going=False
    return

def flip_player():
    global current_player
    
    if current_player =='X':
        current_player='O'
    elif current_player =='O':
        current_player='X'

    return








play_game()





#board
#display board
#play game
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player



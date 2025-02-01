#Start the game by choosing a person to start first by typing "X" or "O"
#Type desired index for placement
#After index is checked appropriately, O or X is recorded on the board
#Other user do the same process
#Play game until one shape appears three times in a row
# O O O    O                  O
#       or    O      or       O   same for x
#               O             O

#If board is full and not finished, it is tie



current_board=[["-", "-", "-"],
               ["-", "-", "-"], 
               ["-", "-", "-"]]
#Initialize board with "-"
def main():

    
    print("Hello! Let's play Tic Tac Toe!! ><")
    print("This is the starting board:")
    print_board(current_board)
    turn_choose()
    return None
  



def print_board(board):
    print("------------")
    for r in range(len(board)):
        line = "| "
        for c in range(len(board)):
            line += board[r][c] + " | "
        print(line)
        print("------------")

#print board shape
    
def update_board(new_value):
    if new_value=="X":
        row_index,col_index=index_CheckX()
        next_new_value="O"

    elif new_value=="O":
        row_index, col_index=index_CheckO()
        next_new_value="X"
      
    #Based on new value, indexCheck function is called.
    #Then, assign next value to be opposite of current new value
  
    if(current_board[row_index][col_index]=="-"):
        current_board[row_index][col_index]=new_value
    else:
        print("This position is taken by other players. Please choose other position again.")
        update_board(new_value)

  #Once a spot is taken, user cannot replace with "O" or "X"
  
    print("This is the updated board:")
    print_board(current_board)

    if check_for_win(current_board)!=None:
        print(check_for_win(current_board))
        return None

    elif check_for_tie(current_board):
        print("There is no winner. Game is over.")
        return None
    
    else:
        update_board(next_new_value)

#Call check_for_win and check_for_tie to see the status of game. If it is not finished, call update_board funciton.

def index_CheckX():
    row_index, col_index=map(int,input(" Write the index you want to add X ").split())
    while(row_index>2 or row_index<0 or col_index<0 or col_index>2 ):
        print("Sorry that is not a valid position. Please reenter the position.")
        row_index, col_index=map(int,input(" Write the index you want to add X ").split())

    return row_index,col_index

        
def index_CheckO():
    row_index, col_index=map(int,input(" Write the index you want to add O ").split())
    while(row_index>2 or row_index<0 or col_index<0 or col_index>2 ):
        print("Sorry that is not a valid position. Please reenter the position.")
        row_index, col_index=map(int,input(" Write the index you want to add O ").split())

    return row_index,col_index

#Check if the input index is an appropriate index. If not, ask for index until it is appropriate.


def check_for_win(board):
    # Check for horizontal lines
     for row in board:

        if all(cell == "X" for cell in row):
            return ("X is a winner!")
    
        elif all(cell == "O" for cell in row):
            return ("O is a winner!")
        
     for col in range(3):

        if all(board[row][col] == "X" for row in range(3)):
            return "X is a winner!"
        
        elif all(board[row][col] == "O" for row in range(3)):
            return "O is a winner!"
        
     if all(board[i][i] == "X" for i in range(3)) or all(board[i][2 - i] == "X" for i in range(3)):
        return "X is a winner!"
     elif all(board[i][i] == "O" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
        return "O is a winner!"  

    
     return (None)

    # This function takes a board and returns if there is a winner or not.
    # If there is a winner, return who the winner is. ("O" or "X")
    # If there is no winner, return None
    # It checks for all possible conditions (three horizontal lines, three vertical lines, and two diagonal lines)
 


def check_for_tie(board):

    if any('-' in row for row in board):
        return False  

   
    if check_for_win(board) is None:
        return True  
    
    else:
        return False  


 
    # This function takes a board and returns a boolean value.
    # In Tic Tac Toe, the game can end without a winner. This function checks if the game ended without a winner.
    # First, check if the board is full. (Checking if we have a "-".)
    # Then, check_for_win. If check_for_win returns None, we have a tie.
    # If we have a tie, return True. If not, return False
    

def turn_choose():
    a=input("Who wants to start first? enter O or X in capital letter ")

    if a=="O":
        print("O plays first, and X plays second.")
        new_value="O"
        update_board( new_value)

    elif a=="X":
        print("X plays first, and O plays second.")
        new_value="X"
        update_board( new_value)

    else:
        print(" Choose either O or X!")
        turn_choose()
    return None

# Determine who is going to start first between "O" and "X".

main()

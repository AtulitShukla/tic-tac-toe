"""Atulit Shukla
SAPID:500075930
CSE AIML B2
R.no.:56"""




board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentplayer = "X"
game=True        #Checks if the game is going on or not
def play_game():

  display_board()
  while game:
      turn(currentplayer)
      gamestats()
      flip_player()
  if winner == "X" or winner == "O":
      print(winner + " won.")
  elif winner == None:
      print("Tie.")
      
def display_board():                     #Function to display the game board to the screen
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")
def gamestats():
    checkwin()
    check_tie()
def turn(player):
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("invalid choice!")
        position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")
  board[position] = player
  display_board()
  
def checkwin():                            #Function to check for a winner
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
    
def check_rows():                          #Function to check rows for a win
  global game
  #this condition will check if any element of rows is blank and if so then wold terminate the traversing through the rows for a win
  r1 = board[0] == board[1] == board[2] != "-"
  r2 = board[3] == board[4] == board[5] != "-"
  r3 = board[6] == board[7] == board[8] != "-"
  if r1 or r2 or r3:
    game = False
  if r1:
    return board[0] 
  elif r2:
    return board[3] 
  elif r3:
    return board[6] 
  else:
    return None

def check_columns():                      #Function to check  the columns for a win
  global game
  #this condition will check if any element of columns is blank and if so then wold terminate the traversing through the columns for a win
  c1 = board[0] == board[3] == board[6] != "-"
  c2 = board[1] == board[4] == board[7] != "-"
  c3 = board[2] == board[5] == board[8] != "-"
  if c1 or c2 or c3:
    game = False
  if c1:
    return board[0] 
  elif c2:
    return board[1] 
  elif c3:
    return board[2] 
  else:
    return None

def check_diagonals():                   #Function to check the diagonals for a win
  global game
  d1 = board[0] == board[4] == board[8] != "-"          #this condition will check if any element of diagonal is blank 
  d2 = board[2] == board[4] == board[6] != "-"          #and if so then wold terminate the traversing through the diagonals for a win
  if d1 or d2:
    game = False
  if d1:
    return board[0] 
  elif d2:
    return board[2]
  else:
    return None

def check_tie():                    #Function to check for a tie
  global game
  if "-" not in board:
    game = False
    return True
  else:
    return False

def flip_player():                       #Function to switch to next player
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    elif currentplayer == "O":
        currentplayer = "X"

play_game()

        

    
    
    

  

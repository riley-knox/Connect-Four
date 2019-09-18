#include python3 print function
from __future__ import print_function

#include numpy
import numpy as np

#define player names and colors
players = {'player1':['A','X'],'player2':['B','R']}
#define the board size
rows = 6
cols = 7
#define the height of each column
columnHeights = [rows,rows,rows,rows,rows,rows,rows]
#start the game with zero turns played
numTurns = 0
#win-checking definitions
row_indices = range(4) #row starting indices in which a horizontal victory is possible (columns 1-4)
col_indices = range(3) #column starting indices in which a vertical victory is possible (rows 1-3)
win_rows = range(rows) #rows in which a horizontal victory is possible (all of them)
win_cols = range(cols) #columns in which a vertical victory is possible (all of them)
diag_cols = range(4) #columns in which a diagonal victory is possible (columns 1-4)
diag_rows_down = range(3) #rows in which a downward diagonal victory is possible (top 3 rows)
diag_rows_up = range(3,rows)[::-1] #rows in which an upward diagonal victory is possible (bottom 3 rows)

#create board as 6x7 zeros array
board = np.chararray((rows,cols))
board[:] = 0
print(board)

#play the game!
while True:

    #determine who's turn it is
    if numTurns % 2 != 0:
        player = players['player2'][0]
        playerID = players['player2'][1]
    else:
        player = players['player1'][0]
        playerID = players['player1'][1]

    #take player's input
    while True:
        #check to make sure it's an integer
        while True:
            try:
                play = int(input("Player {}, it's your turn! Pick a column: ".format(player)))
                break
            except NameError:
                print('Enter an integer from 1 to 7!')
        #check to make sure it's within the board
        if play < 1 or play > 7:
            print('Enter an integer from 1 to 7!')
        else:
            pass
        #check to make sure the column has an empty space
        if columnHeights[play-1] == 0:
            print("That column is full! Pick another.")
        else:
            break

    #determine positioning of play
    playCol = play-1
    playRow = columnHeights[playCol]-1

    #place player's color in lowest open column space
    board[playRow,playCol] = playerID

    #update the column heights
    columnHeights[playCol] = columnHeights[playCol]-1

    #update the number of turns
    numTurns += 1

    #display the new board
    print(board)

    #check to see if somebody wins
    #horizontal first
    for i in win_rows:
        for j in row_indices:       #scan row indices where victory is possible (columns 1-4)
            chunk = range(j,j+4)    #create 4-index chunk
            slot = board[i,chunk]   #create "victory slot" from chunk indices
            if all(x == playerID for x in slot):            #check if all values in slot are one player's pieces
                print("Player {} wins!".format(player))     #print victory message
                quit()
            else:
                j += 1              #if no victory, move to next column where victory is possible
        i += 1                      #if no victory, move to the next row
    #vertical next
    #functions the same as horizontal victory loop, but rows & columns are switched
    for i in win_cols:
        for j in col_indices:       #scan column indices where victory is possible (rows 1-3)
            chunk = range(j,j+4)
            slot = board[chunk,i]
            if all(x == playerID for x in slot):
                print("Player {} wins!".format(player))
                quit()
            else:
                j += 1              #if no victory, move to next row where victory is possible
        i += 1                      #if no victory, move to the next column
    #downward diagonal next
    #functions the same as horizontal/vertical victory loops, but includes row- and column-wise iteration in each loop
    for i in diag_cols:                 #scan starting columns where diagonal victory is possible (#s 1-4)
        chunk_cols = range(i,i+4)       #generate chunk of columns being checked for diagonal victory
        for j in diag_rows_down:        #scan starting rows where victory is possible (top 3 rows)
            chunk_rows = range(j,j+4)   #generate chunk of rows being checked for diagonal victory
            slot = [board[chunk_rows[0],chunk_cols[0]],board[chunk_rows[1],chunk_cols[1]],board[chunk_rows[2],chunk_cols[2]],board[chunk_rows[3],chunk_cols[3]]]    #create "victory slot" from chunk indices
            if all(x == playerID for x in slot):            #check if all values in slot are one player's pieces
                print("Player {} wins!".format(player))
                quit()
            else:
                j += 1                  #if no victory, move to the next row where victory is possible
        i += 1                          #if no victory, move to the next column where victory is possible
    #upward diagonal next
    #functions the same as downward diagonal victory loop, but checks rows starting from the bottom
    for i in diag_cols:                 #scan starting columns where diagonal victory is possible (#s 1-4)
        chunk_cols = range(i,i+4)       #generate chunk of columns being checked for diagonal victory
        for j in diag_rows_up:          #scan starting rows where victory is possible (bottom 3 rows)
            chunk_rows = range(j-3,j+1)[::-1]   #generate chunk of rows being checked for diagonal victory
            slot = [board[chunk_rows[0],chunk_cols[0]],board[chunk_rows[1],chunk_cols[1]],board[chunk_rows[2],chunk_cols[2]],board[chunk_rows[3],chunk_cols[3]]]    #create "victory slot" from chunk indices
            if all(x == playerID for x in slot):            #check if all values in slot are one player's pieces
                print("Player {} wins!".format(player))
                quit()
            else:
                j += 1                  #if no victory, move to the next row where victory is possible
        i += 1                          #if no victory, move to the next column where victory is possible

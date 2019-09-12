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
h_v_indices = range(4) #row/column starting indices in which a horizontal or vertical victory is possible
win_rows = range(rows) #rows in which a horizontal victory is possible (all of them)
win_cols = range(cols) #columns in which a vertical victory is possible (all of them)

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
        for j in h_v_indices:
            chunk = range(j,j+4)
            slot = board[i,chunk]
            if all(x == playerID for x in slot):
                print("Player {} wins!".format(player))
                quit()
            else:
                j += 1
        i += 1

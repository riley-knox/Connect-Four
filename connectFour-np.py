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

    #display the new board
    print(board)

    #update the column heights
    columnHeights[playCol] = columnHeights[playCol]-1
    print(columnHeights)

    #update the number of turns
    numTurns += 1

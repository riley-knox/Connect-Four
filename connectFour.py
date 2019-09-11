#include python3 print function
from __future__ import print_function

#define each row as a list of zeros
columns = [0,0,0,0,0,0,0]
#define number of rows
rows = 6
#define height of each column
columnHeights = [rows,rows,rows,rows,rows,rows,rows]
#define player names and colors
players = {'player1':['A','X'],'player2':['B','R']}
#start the game with zero turns played
numTurns = 0

#generate blank board
for i in range(rows):
    print(columns)

#play the game!
while True:
#determine who's turn it is
    if numTurns % 2 != 0:
        player = players['player2'][0]
    else:
        player = players['player1'][0]
#take player's input
    while True:
        #check to make sure it's an integer
        while True:
            try:
                play = int(input('Player {}, it''s your turn! Pick a column: '.format(player)))
                break
            except NameError:
                print('Enter an integer from 1 to 7!')
        #check to make sure it's within the board
        if play < 1 or play > 7:
            print('Enter an integer from 1 to 7!')
        else:
            break

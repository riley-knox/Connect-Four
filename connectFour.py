#include python3 print function
from __future__ import print_function

#define each row as a list of zeros
columns = [0,0,0,0,0,0,0]
#define number of rows
rows = 6
#define player names and colors
players = {'player1':['A','X'],'player2':['B','O']}
#start the game with zero turns played
numTurns = 0

#generate blank board
for i in range(rows):
    print(columns)

#determine who's turn it is
if numTurns % 2 != 0:
    player = players['player1'][0]
else:
    player = players['player2'][0]

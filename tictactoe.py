import random

def printboard():
    print()
    for row in board:
        for col in row:
            print(col, end = '   ')
        print('')
    print()
    
#----------------------------------------------------------------------------------------------------------------------------------------#

one = '1'
two = '2'
three = '3'
four = '4'
five = '5'
six = '6'
seven = '7'
eight = '8'
nine = '9'

pl1 = 'X'
pl2 = 'O'

board = [
    [one,'  |',two,'  |', three],
    ['-','  +','-','  +','-'],
    [four,'  |',five,'  |',six],
    ['-','  +','-','  +','-'],
    [seven,'  |',eight,'  |',nine]
]

printboard()

while True:
    while True:
        x = input('<Player1> ')
        if x == '1':
            board[0][0] = pl1
        if x == '2':
            board[0][2] = pl1
        if x == '3':
            board[0][4] = pl1
        if x == '4':
            board[2][0] = pl1
        if x == '5':
            board[2][2] = pl1
        if x == '6':
            board[2][4] = pl1
        if x == '7':
            board[4][0] = pl1
        if x == '8':
            board[4][2] = pl1
        if x == '9':
            board[4][4] = pl1
        else:
            print('')

    printboard()

    o = input('<Player2> ')
    if o == '1':
        if board[0][0] == one:
            board[0][0] = pl2
            break
        else:
            print('That spot is alreadly taken')
    if o == '2':
        board[0][2] = pl2
    if o == '3':
        board[0][4] = pl2
    if o == '4':
        board[2][0] = pl2
    if o == '5':
        board[2][2] = pl2
    if o == '6':
        board[2][4] = pl2
    if o == '7':
        board[4][0] = pl2
    if o == '8':
        board[4][2] = pl2
    if o == '9':
        board[4][4] = pl2
        
    printboard()

    





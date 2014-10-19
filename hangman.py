import wordlist

print('Loading random word...')
randomword = wordlist.randomword()

def printman():
    wordnumber = 0
    wordletters = ''
    
    for letter in randomword:
        wordletters = wordletters + '_ '
        
    for letter in wordletters:
        wordnumber = wordnumber + 1
    wordnumber = wordnumber / 2

    head = 'O'
    bodyone = '+'
    bodytwo = '|'
    bodythree = ' -   -   -'
    leftarm = '-'
    rightarm = '-'
    rightleg =' |'
    leftleg = '|'
    man = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [wordletters]
    ]
    for row in man:
        for col in row:
            print(col, end = '   ')
        print('')
##############################################
while True:
    printman()
    letter = input('>>> ').strip().lower()
    if letter == randomword:
        print('you guessed the word!')
        break
    elif letter == '':
        print('false')
    elif letter in randomword:
        print('correct')
    elif letter == 'i give up':
        print('The word was: ' + randomword)
        break
    else:
        print('false')


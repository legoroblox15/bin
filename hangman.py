import wordlist
difficultymax = input('Maximum letters?\n>>> ')
difficultymin = input('Minimum letters?\n>>> ')
difficultymax = int(difficultymax)
difficultymin = int(difficultymin)
print('Loading random word...')
while True:
    lettercount = 0
    randomword = wordlist.randomword()
    for letter in randomword:
        lettercount = lettercount + 1
    if lettercount >= difficultymin and lettercount <= difficultymax:
        break
randomword = randomword.upper()
correct_letters = []
incorrect_letters = []
randomwordlist = []
wordblanks = []
trys = 0
for letter in randomword:
    print('_', end=' ')
print()
def blanks(guess, randomword):
    placevalue = 0
    repeat = 0
    
    for letter in randomword:
        if guess in letter:
            if guess in correct_letters:
                already_guessed = 1
            else:
                correct_letters.append(guess)
                already_guessed = 0
        else:
            if guess in incorrect_letters:
                already_guessed = 1
            else:
                incorrect_letters.append(guess)
                already_guessed = 0
    if '' in correct_letters:
        correct_letters.remove('')
    
    for letter in randomword:
        wordblanks.append('_')
                
    for letter in correct_letters:
        for wordletter in randomword:
            if wordletter == letter:
                wordblanks.pop(placevalue)
                wordblanks.insert(placevalue, letter)
            placevalue = placevalue + 1
        placevalue = 0
    print('Guessed leters: ')
    for letter in incorrect_letters:
        print(letter, end=' ')
    print()
    for letter in wordblanks:
        print(letter, end=' ')
    print()
    wordblanks.clear()

while True:
    guess = input('>>> ')
    trys = trys + 1
    guess = guess.strip().upper()
    if guess == randomword:
        print('Congradulations! you guessed ' + randomword + ' in ' + str(trys) + ' trys!')
        break
    if guess == 'I GIVE UP':
        print('The word was: ' + randomword)
        break
    blanks(guess, randomword)


import words

print('Loading random word...')
randomword = words.randomword()

while True:
    letter = input('>>> ').strip().lower()
    if letter == randomword:
        print('you guessed the word')
    elif letter in randomword:
        print('correct')
    elif letter == 'i give up':
        print('The word was: ' + randomword)
    else:
        print('false')

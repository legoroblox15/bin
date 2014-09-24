import random
import time
wordfile = open('C:\words.txt')

words = []
for line in wordfile:
    for word in wordfile:
        word = word.strip()
        words.append(word)

def randomword():
    randomword = random.choice(words)
    return randomword

        


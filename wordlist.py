# For this to work you need the folder named 'words' that contains all
# the 'txt' files, when you get this folder, put it in your 'C' drive.
# This Python file itself must be in the same folder as the python file you are importing this to.
# The words folder takes up about 1150KB of storage.
import random
wordfile = open('C:\words\words.txt')
adjfile = open('C:\words\jectives.txt')                 # If you are wondering why the first letters are
verbfile = open('C:\words\erbs.txt')                    # left out in some of these 'txt' files, it's because Python
adverbfile = open('C:\words\dverbs.txt')             # will give an error otherwise
nounfile = open('C:\words\ouns.txt')
pronounfile = open('C:\words\pronouns.txt')

adjs = []
words = []
verbs = []
adverbs = []
pronouns = []
nouns = []

for line in wordfile:
    for word in wordfile:
        word = word.strip()
        words.append(word)

for line in adjfile:
    for word in adjfile:
        word = word.strip()
        adjs.append(word)

for line in verbfile:
    for word in verbfile:
        word = word.strip()
        verbs.append(word)

for line in adverbfile:
    for word in adverbfile:
        word = word.strip()
        adverbs.append(word)

for line in pronounfile:
    for word in pronounfile:
        word = word.strip()
        pronouns.append(word)

for line in nounfile:
    for word in nounfile:
        word = word.strip()
        nouns.append(word)
        
def allwords():
    return words
# Syntax for assigning this to a variable: variable = wordlist.allwords()

def alladjs():
    return adjs
# Syntax for assigning this to a variable: variable = wordlist.alladjs()

def allverbs():
    return verbs
# Syntax for assigning this to a variable: variable = wordlist.allverbs()

def alladverbs():
    return adverbs
# Syntax for assigning this to a variable: variable = wordlist.allverbs()

def allpronouns():
    return pronouns
# Syntax for assigning this to a variable: variable = wordlist.allpronouns()

def allnouns():
    return nouns
# Syntax for assigning this to a variable: variable = wordlist.allnouns()

def randomword():
    randomword = random.choice(words)
    return randomword
# Syntax for assigning this to a variable: variable = wordlist.randomword()

def randomadj():
    randomadj = random.choice(adjs)
    return randomadj
# Syntax for assigning this to a variable: variable = wordlist.randomadj()

def randomverb():
    randomverb = random.choice(verbs)
    return randomverb
# Syntax for assigning this to a variable: variable = wordlist.randomverb()

def randomadverb():
    randomadverb = random.choice(adverbs)
    return randomadverb
# Syntax for assigning this to a variable: variable = wordlist.randomadverb()

def randompronoun():
    randompronoun = random.choice(pronouns)
    return randompronoun
# Syntax for assigning this to a variable: variable = wordlist.randompronoun()

def randomnoun():
    randomnoun = random.choice(nouns)
    return randomnoun
# Syntax for assigning this to a variable: variable = wordlist.randomnoun()

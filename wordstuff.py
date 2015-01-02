import wordlist
def palindromes():
    words = wordlist.allwords()
    palindrome = []
    wordaslist = []
    palindromes = 0
    for word in words:
        palindrome.clear()
        wordaslist.clear()
        for letter in word:
            palindrome.insert(0, letter)
            wordaslist.append(letter)
        if wordaslist == palindrome:
            for letter in palindrome:
                print(letter, end='')
            print()
            palindromes = palindromes + 1
    print(str(palindromes))
def anagrams():
    examples = wordlist.allwords()
    anagrams = []
    anagramnumber = 0
    for trialword in examples:
        for word in examples:
            correctletter = 0
            incorrectletter = 0
            wordlength = 0
            dontcount = 0
            if trialword == word:
                dontcount = 1
            for letter in trialword:
                if letter in word:
                    correctletter = correctletter + 1
                else:
                    incorrectletter = incorrectletter + 1
            for letter in word:
                wordlength = wordlength + 1
            if wordlength == correctletter + incorrectletter:
                if incorrectletter == 0:
                    if trialword in anagrams:
                        dontcount = 1
                    if dontcount == 0:
                        anagrams.append(trialword)
    for anagram in anagrams:
        print(anagram, end='')
        print()
    for anagram in anagrams:
        anagramnumber = anagramnumber + 1
    print(anagramnumber)
anagrams()
            

import wordlist
import time

while True:
    adjective = wordlist.randomadj()
    noun = wordlist.randomnoun()
    verb = wordlist.randomverb()
    adverb = wordlist.randomadverb()
    a = "{} {}"
    a = a.format(adjective, noun)
    print(a)
    time.sleep(2)



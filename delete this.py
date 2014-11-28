import wordlist
import time

while True:
    adjective = wordlist.randomadj()
    a_noun = wordlist.randomnoun()
    b_noun = wordlist.randomnoun()
    a = "{}s comes form {} {}s"
    a = a.format(a_noun, adjective, b_noun)
    print(a)
    time.sleep(7)



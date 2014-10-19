import wordlist

while True:
    noun = wordlist.randomnoun()
    adj = wordlist.randomadj()
    a = '{} {}'
    a = a.format(adj, noun)
    print(a)
    input()



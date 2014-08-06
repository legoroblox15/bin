import random
numb = 0
while True:
    numb = numb + 1
    roll = random.randint(1,100)
    if roll == 1:
        trys = "It took {} try(s) to get the number 1".format(numb)
        print(trys)
        break


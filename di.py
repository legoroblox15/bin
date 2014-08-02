import random
numb = 0
while True:
    numb = numb + 1
    roll = random.randrange(1,1001)
    pr = "{}. {}".format(numb,roll)
    print(pr)
    if roll == 1:
        break

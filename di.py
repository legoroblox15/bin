import random
numb = 0
while True:
    numb = numb + 1
    roll = random.randint(1,1000)
    pr = "{}. {}".format(numb,roll)
    print(pr)
    if roll == 1:
        break

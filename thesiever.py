print('Welcome to The Siever (dramatic sound)')
while True:
    print('Would you like to start a new game or import a saved game')
    setgame = input('>>> ')
    setgame = setgame.strip().lower()
    if setgame == 'new game':
        break
    if setgame == 'import game':
        print('Sorry, that feature is not implemented yet.')
    else:
        print('That is not a command')
while True:
    command = input("Where would you like to go? Type 'help' to find a list of places along with some useful commands\n>>> ")
    command = command.strip().lower()
    if command == 'help':
        print(
'''
places you can go: the mines, your sieve, your tumbler, your cutter, your shop

useful commands: stats, info <thing>

stats: tells you your current statistics e.g: money, equipment

info <thing>: tells you about something, just type 'info' then a thing you want to know about or type
'info the siever' to learn what this game is about
'''
)
    elif command == 'info the siever':
        print(
'''
In this game, you are a grumpy old rock collecter that wants to make a fortune by selling rocks. You first need
to buy some gravel, sieve it for it's resources, tumble the ores to make it pollished, cut the ores so they look
even nicer, then finally sell your masterpieces for a profit. Use the money to buy more gravel and even better
equipment and repeat the process. Can you become the richest person in the WORLD?
'''
)
    elif command == 'info the mines':
        print(
'''
Go here to buy gravel and better equipment. Better equipment and gravel makes your rocks more valuable. 
'''
)
    elif command == 'info your sieve':
        print(
'''
Go here to sieve your newly purchased gravel into rocks you can refine and sell. The better your gravel is, the
more rocks you will get. Sieving takes a while, so upgrade your sieve so you can sieve faster and get even
more rocks to sell
'''
)
    elif command == 'info your tumbler':
        print(
'''
Tumble the rocks that you just collected to give them a polished look so they can be more valuable. tumbling
takes a while and can be really tedious considering you can only sieve a few rocks at a time, but if you
upgrade your tumbler your rocks will not only become more valuable, it will be faster and you can tumble more
at a time.
'''
)
    elif command == 'info your cutter':
        print(
'''
You have now tumbled your rocks and they look nice and dandy, but something is missing. That's where the
cutter comes in. With the cutter, you can cut rocks into specific shapes and sizes so it can fit in jewlery,
making your rocks' value go up significantly. Cutting rocks can take a while and can sometimes only cut
certain types of rocks, but if you upgrade your cutter you can not only cut things faster, you can cut more
types of rocks and can even make your rocks more valuable.
'''
)
    elif command == 'info your shop':
        print(
'''
Now is the moment you've been waiting for, you've put so much time and effort into these rocks, that you just
can't wait to sell them and roll in the cash, but remeber, the more effort you put in your rocks, the more money
you get.
'''
)
    else:
        print('That is not a command')

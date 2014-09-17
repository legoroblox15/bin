import random
import time
import math
import VIRUS
#----------------------------------------------------------------------------------------------------------------------------------------#
def shutdown():
    print('''
Shuting down...''')
    time.sleep(3)
#----------------------------------------------------------------------------------------------------------------------------------------#
def help():
    
    print('''
Commands you can use at this section: math, 8ball, rpsls, lucky#s

About: welecome to Pybot(TM) fell free to explore!

Commands you can use all the time (and what they do):

return: will take you back a section (if you type return at home, it will do a shutdown sequence)

help: will tell you all the avalable commands in that section
''')
#----------------------------------------------------------------------------------------------------------------------------------------#
def math():
    def calculater():
        def calculaterhelp():
            print('''
Functions you can use at this section (and what they do): +, -, *, /, ^, /=

+: adds up the numbers
-: finds the difference of numbers
*: adds one of the numbers the amount of times the other number is worth
/: splits one of the numbers the amount of times the other nimber is worth
^: finds the power of a number
/=: finds the root of a number

Syntax: 1st# func 2nd#. Remember to put spaces inbetween, and only 1 operation at a time 

About: just a same-old same-old calculater; able to use answers from a previous problem and
save it, just type 'Ans' where your number should be; can use decimals but not fractions!

Commands you can use all the time (and what they do):

return: will take you back a section (if you type return at home, it will do a shutdown sequence)

help: will tell you all the avalable commands in that section
''')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
        while True:
            
            equation = input('''
What is you equation?\nHome>Math>Calculater> ''')

            equation = equation.strip()
            equation = equation.lower()
            
            if '+' in equation:
                a = a
            elif '-' in equation:
                a = a
            elif '*' in equation:
                a = a
            elif '/' in equation:
                a = a
            elif '**' in equation:
                a = a
            elif '/=' in equation:
                a = a
            elif equation == 'help':
                calculaterhelp()
            elif equation == 'return':
                break
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
            else:
                print('''
Error! try again''')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#    
    def mathhelp():
        print('''
Commands you can use at this section: calculater, speed, acceleration

About: find answers to math problems!

Commands you can use all the time (and what they do):

return: will take you back a section (if you type return at home, it will do a shutdown sequence)

help: will tell you all the avalable commands in that section
''')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
    while True:
        
        operation = input('''
What would you like to use?\nHome>Math> ''')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#        
        operation = operation.strip()
        operation = operation.lower()

        if operation == 'help':
            mathhelp()
        elif operation == 'return':
            break
        elif operation == 'calculater':
            calculater()
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
        else:
            print('''
That is not a command, for a list of all the commands, type 'help' ''')
        
#----------------------------------------------------------------------------------------------------------------------------------------#

while True:
    command = input('''
Hello, I am Pybot, what would you like me to do? for a list of all the
commands, type 'help'\nHome> ''')

    command = command.strip()
    command = command.lower()
#----------------------------------------------------------------------------------------------------------------------------------------#
    if command == 'help':
        help()
    elif command == 'math':
        math()
    elif command == 'return':
        shutdown()
        break
    elif command == 'virus':
        VIRUS.virus()
#----------------------------------------------------------------------------------------------------------------------------------------#
    else:
        print('''
That is not a command, for a list of all the commands, type 'help' ''')


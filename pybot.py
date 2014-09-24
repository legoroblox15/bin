import random
import time
import math
import VIRUS

##Pybot 1.0
##Made by legoroblox15
##Contributers: ender_wing for idea for contributers list :)
##MrRob for teching me python :D
##gabeart10 for insperation
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
    def shape():
        def shapehelp():
            print('''
Commands you can use at this section: 3D, 2D

About: either 2D shapes or 3D shapes, you decide

Commands you can use all the time (and what they do):

return: will take you back a section (if you type return at home, it will do a shutdown sequence)

help: will tell you all the avalable commands in that section
''')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
        def twod():
            def twodhelp():
                print('''
Commands you can use at this section: square, triangle, circle, rhombus, parallelagram

About: either 2D shapes or 3D shapes, you decide

Commands you can use all the time (and what they do):

return: will take you back a section (if you type return at home, it will do a shutdown sequence)

help: will tell you all the avalable commands in that section
    ''')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
        while True:
            dimention = input('''
Is the shape 2D or 3D?\nPybot>Math>Shapes> ''').strip().lower()
            if dimention == 'return':
                break
            elif dimention == 'help':
                shapehelp()
            elif dimention == '3d':
                threed()
            elif dimention ==  '2d':
                twod()
            else:
                print('''
That is not a command, for a list of commands, type 'help' ''')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
            while True:
                dimention = input('''
What shape?\nPybot>Math>Shapes>2D> ''').strip().lower()
                if dimention == 'return':
                    break
                elif dimention == 'help':
                    twodhelp()
                elif dimention == 'return':
                    break
                elif dimention ==  'square':
                    a = a
                else:
                    print('''
That is not a command, for a list of commands, type 'help' ''')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
    def speed():
        while True:
            distance = input('''
What is your distance?\nPybot>Math>Speed> ''')
            if distance == 'help':
                print('''
                           D
Equation:     S = ------
                           T

Note: don't include the unit of messure in your measurements
    
Commands you can use all the time (and what they do):

return: will take you back a section (if you type return at home, it will do a shutdown sequence)

help: will tell you all the avalable commands in that section
''')
            elif distance == 'return':
                break
            else:
                time = input('''
What is your time?\nPybot>Math>Speed> ''')
                distance = float(distance)
                time = float(time)
                speed = distance / time
                speed = str(speed)
                print(speed + ' u/t')
                break
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
    def acceleration():
        while True:
            intialvelocity = input('''
What is your intial velocity?\nPybot>Math>Speed> ''')
            if intialvelocity == 'help':
                print('''
                         Vf    -    Vi
Equation:     A = ---------------
                               T
                               
Note: don't include the unit of messure in your measurements
    
Commands you can use all the time (and what they do):

return: will take you back a section (if you type return at home, it will do a shutdown sequence)

help: will tell you all the avalable commands in that section
''')
            elif intialvelocity == 'return':
                break
            else:
                finalvelocity = input('''
What is your final velocity?\nPybot>Math>Speed> ''')
                time = input('''
What is your time?\nPybot>Math>Speed> ''')
                time = float(time)
                intialvelocity = float(intialvelocity)
                finalvelocity = float(finalvelocity)
                vi_minus_vf = finalvelocity - intialvelocity
                acceleration = vi_minus_vf / time
                acceleration = str(acceleration)
                print(acceleration + ' u/t^2')
                break
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
    def force():
        while True:
            mass = input('''
What is your mass?\nPybot>Math>Speed> ''')
            if mass == 'help':
                print('''    
Equation:     F = ma

Note: don't include the unit of messure in your measurements
    
Commands you can use all the time (and what they do):

return: will take you back a section (if you type return at home, it will do a shutdown sequence)

help: will tell you all the avalable commands in that section
''')
            elif mass == 'return':
                break
            else:
                acceleration = input('''
What is your acceleration?\nPybot>Math>Speed> ''')
                mass = float(mass)
                acceleration = float(acceleration)
                force = mass * acceleration
                force = str(force)
                print(force + ' N')
                break

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
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
What is you equation?\nPybot>Math>Calculater> ''')

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
            elif '^' in equation:
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
Commands you can use at this section: calculater, speed, acceleration, force, shape

About: find answers to math problems!

Commands you can use all the time (and what they do):

return: will take you back a section (if you type return at home, it will do a shutdown sequence)

help: will tell you all the avalable commands in that section
''')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
    while True:
        
        operation = input('''
What would you like to use?\nPybot>Math> ''')
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#        
        operation = operation.strip()
        operation = operation.lower()

        if operation == 'help':
            mathhelp()
        elif operation == 'return':
            break
        elif operation == 'calculater':
            calculater()
        elif operation == 'speed':
            speed()
        elif operation == 'acceleration':
            acceleration()
        elif operation == 'force':
            force()
        elif operation == 'shape':
            shape()
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#
        else:
            print('''
That is not a command, for a list of all the commands, type 'help' ''')
        
#----------------------------------------------------------------------------------------------------------------------------------------#

while True:
    command = input('''
Hello, I am Pybot, what would you like me to do? for a list of all the
commands, type 'help'\nPybot> ''')

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


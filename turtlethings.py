import turtle
import mymod

bob = turtle.Turtle()

bob.speed(0)
bob.pensize(3)

def colrscreen():
    for count in range(1, 720):
        bob.pencolor(mymod.randomcolor())
        bob.forward(5000)
        bob.backward(5000)
        bob.right(.5)

def donut():
    for count in range(1, 360):
        bob.pencolor(mymod.randomcolor())
        bob.forward(100)
        bob.backward(200)
        bob.forward(101)
        bob.right(1)

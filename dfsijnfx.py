import turtle
bob = turtle.Turtle()
bob.pensize(1)
bob.speed(0.1)
bob.pencolor(1, .5, 0)
for i in range(530):
    bob.forward(i)
    bob.right(90)
bob.pu()
bob.goto(0, 0)
bob.pd()
bob.pencolor(1, 0, 1)
for i in range(530):
    bob.forward(i)
    bob.right(90)

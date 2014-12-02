import turtle

bob = turtle.Turtle()

bob.speed(0)
bob.pensize(7)
bob.left(90)
bob.pu()
bob.forward(334.3949044585987)
bob.pd()
bob.right(90)
bob.ht()
for count in range(0, 100): ## Red to yellow
    count = count / 100
    bob.pencolor(1, count, 0)
    bob.forward(3.5)
    bob.right(.6)
for count in range(0, 100): ## Yellow to lime 
    count = count / 100
    count = 1 - count
    bob.pencolor(count, 1, 0)
    bob.forward(3.5)
    bob.right(.6)
for count in range(0, 100): ## Lime to Indigo
    count = count / 100
    bob.pencolor(0, 1, count)
    bob.forward(3.5)
    bob.right(.6)
for count in range(0, 100): ## Indigo to blue
    count = count / 100
    count = 1 - count
    bob.pencolor(0, count, 1)
    bob.forward(3.5)
    bob.right(.6)
for count in range(0, 100): ## Blue to magenta
    count = count / 100
    bob.pencolor(count, 0, 1)
    bob.forward(3.5)
    bob.right(.6)
for count in range(0, 100): ## Magenta to red
    count = count / 100
    count = 1 - count
    bob.pencolor(1, 0, count)
    bob.forward(3.5)
    bob.right(.6)

## Diameter: About 668.7898089171974
## Radius: About 334.3949044585987
## Circum: 2100

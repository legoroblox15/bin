import turtle

bob = turtle.Turtle()

bob.speed(0)
bob.ht()
for count in range(100): ## Red to yellow
    bob.pensize(1202 - count * 2)
    count = count / 100
    bob.pencolor(1, count, 0)
    bob.forward(1)
    bob.backward(1)
for count in range(100): ## Yellow to green
    bob.pensize(1002 - count * 2)
    count = count / 100
    count = 1 - count
    bob.pencolor(count, 1, 0)
    bob.forward(1)
    bob.backward(1)
for count in range(100): ## Green to Indigo
    bob.pensize(802 - count * 2)
    count = count / 100
    bob.pencolor(0, 1, count)
    bob.forward(1)
    bob.backward(1)
for count in range(100): ## Indigo to blue
    bob.pensize(602 - count * 2)
    count = count / 100
    count = 1 - count
    bob.pencolor(0, count, 1)
    bob.forward(1)
    bob.backward(1)
for count in range(100): ## Blue to magenta
    bob.pensize(402 - count * 2)
    count = count / 100
    bob.pencolor(count, 0, 1)
    bob.forward(1)
    bob.backward(1)
for count in range(100): ## Magenta to red
    bob.pensize(202 - count * 2)
    count = count / 100
    count = 1 - count
    bob.pencolor(1, 0, count)
    bob.forward(1)
    bob.backward(1)
## Diameter: About 668.7898089171974
## Radius: About 334.3949044585987
## Circum: 2100

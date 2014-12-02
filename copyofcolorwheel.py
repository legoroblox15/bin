import turtle

bob = turtle.Turtle()

bob.speed(0)
bob.pensize(3)
bob.left(90)

bob.ht()
for count in range(0, 100): ## Black to red
    count = count / 100
    bob.pencolor(count, 0, 0)
    bob.forward(3.343949044585987)
bob.right(90)
for count in range(0, 100): ## Red to yellow
    count = count / 100
    bob.pencolor(1, count, 0)
    bob.forward(3.5)
    bob.right(.6)
bob.right(90)
for count in range(0, 100): ## Yellow to black
    count = count / 100
    count = 1 - count
    bob.pencolor(count, count, 0)
    bob.forward(3.343949044585987)
for count in range(0, 100): ## Black to yellow
    count = count / 100
    count = count
    bob.pencolor(count, count, 0)
    bob.backward(3.343949044585987)
bob.left(90)
for count in range(0, 100): ## Yellow to green 
    count = count / 100
    count = 1 - count
    bob.pencolor(count, 1, 0)
    bob.forward(3.5)
    bob.right(.6)
bob.right(90)
for count in range(0, 100): ## Green to black 
    count = count / 100
    count = 1 - count
    bob.pencolor(0, count, 0)
    bob.forward(3.343949044585987)
for count in range(0, 100): ## Black to green 
    count = count / 100
    bob.pencolor(0, count, 0)
    bob.backward(3.343949044585987)
bob.left(90)
for count in range(0, 100): ## Green to Blue
    count = count / 100
    bob.pencolor(0, 1, count)
    bob.forward(3.5)
    bob.right(.6)
bob.right(90)
for count in range(0, 100): ## Blue to black 
    count = count / 100
    count = 1 - count
    bob.pencolor(0, count, count)
    bob.forward(3.343949044585987)
for count in range(0, 100): ## Black to blue
    count = count / 100
    bob.pencolor(0, count, count)
    bob.backward(3.343949044585987)
bob.left(90)
for count in range(0, 100): ## Blue to indigo
    count = count / 100
    count = 1 - count
    bob.pencolor(0, count, 1)
    bob.forward(3.5)
    bob.right(.6)
bob.right(90)
for count in range(0, 100): ## Indigo to black 
    count = count / 100
    count = 1 - count
    bob.pencolor(0, 0, count)
    bob.forward(3.343949044585987)
for count in range(0, 100): ## Black to Indigo
    count = count / 100
    bob.pencolor(0, 0, count)
    bob.backward(3.343949044585987)
bob.left(90)
for count in range(0, 100): ## indigo to magenta
    count = count / 100
    bob.pencolor(count, 0, 1)
    bob.forward(3.5)
    bob.right(.6)
bob.right(90)
for count in range(0, 100): ## Magenta to black 
    count = count / 100
    count = 1 - count
    bob.pencolor(count, 0, count)
    bob.forward(3.343949044585987)
for count in range(0, 100): ## Black to Magenta
    count = count / 100
    bob.pencolor(count, 0, count)
    bob.backward(3.343949044585987)
bob.left(90)
for count in range(0, 100): ## Magenta to red
    count = count / 100
    count = 1 - count
    bob.pencolor(1, 0, count)
    bob.forward(3.5)
    bob.right(.6)

## Diameter: About 668.7898089171974
## Radius: About 334.3949044585987
## Circum: 2100

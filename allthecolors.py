import turtle

bob = turtle.Turtle()
#bob.ht()
bob.speed(0)
bob.pensize(1)
bob.left(90)
bob.pu()
bob.backward(300)
bob.pd()

for saturation in range(256):
    saturation = saturation / 255
    for shade in range(256):
        shade = shade / 255
        r = 1
        g = shade + saturation
        if g > 1:
            g = 1
        b = shade
        bob.pencolor(r, g, b)
        bob.forward(1)
    bob.pu()
    bob.backward(512)
    bob.left(90)
    bob.forward(1)
    bob.right(90)
    bob.pd()
        

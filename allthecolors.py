import turtle

bob = turtle.Turtle()
#bob.ht()
bob.speed(0)
bob.pensize(1)

bob.pu()
bob.forward(332)
bob.right(90)
bob.forward(279)
bob.right(180)
bob.pd()
for saturation in range(100):
    for hue in range(201):
        hue = hue / 100
        if hue <= 1:
            r = hue
            if hue <= saturation:
                g = 0
                b = 0
            else:
                g = hue - saturation
                b = hue - saturation
            bob.pencolor(r, g, b)
            bob.forward(1)
        elif hue > 1:
            hue = hue - 1
            r = 1
            g = saturation + hue
            b = saturation + hue
            if saturation + hue >= 1:
                g = 1
                b = 1
            bob.pencolor(r, g, b)
            bob.forward(1)
        
    
        

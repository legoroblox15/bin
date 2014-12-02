def graph():
    # Graphing calculater made by legoroblox15
    
    # Currently only works for: y = mx + b and now supports undefined slopes

    slope = input('slope?\n>>> ').strip().lower()    # 'm'
    if slope == 'undefined':
        inter = input('x intercept?\n>>> ') # 'x'
        undefined = 1
        slope = ''
    else:
        inter = input('y intercept?\n>>> ') # 'b'
        undefined = 0
        
    if slope == '':
        slope = 0
    if inter == '':
        inter = 0
        
    import turtle
    graph = turtle.Turtle()
    line = turtle.Turtle()

    graph.speed(0)
    graph.pencolor('blue')
    graph.pensize(3)
    
    line.speed(0)
    line.pensize(1)
    
    def buildgraph():
        graph.forward(1000)
        graph.backward(2000)
        graph.forward(1000)
        graph.right(90)
        graph.forward(1000)
        graph.backward(2000)
            
    slope = float(slope)
    inter = float(inter)

    line.ht()
    line.pensize(0)
    line.speed(0)

    buildgraph()

    line.pu()
    if undefined == 0:
        line.left(90)
        line.forward(inter * 10)
        line.right(90)
        line.pd()
        if slope < 0:
            negitive = 2
            line.left(90)
            slope = slope * -1
        else:
            negitive = 1

        angle = 90 - ((90 / 2 ** (slope - 1)) / 2)
        
        line.left(angle)
        line.forward(2000)
        line.backward(4000)
        line.forward(2000)
        line.right(angle + 90 * negitive)
        line.pu()
        line.forward(inter * 10)
        line.left(90)
        line.pd()
    elif undefined == 1:
        line.forward(inter * 10)
        line.left(90)
        line.pd()
        line.forward(2000)
        line.backward(4000)
        line.forward(2000)
        line.pu()
        line.right(90)
        line.backward(inter * 10)
        line.pd()
while True:
    graph()

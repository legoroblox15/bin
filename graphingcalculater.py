def graph():
    # Graphing calculater made by legoroblox15, graph is at a 10:1 scale
    undef = 0

    # Currently only works for: y = mx + b

    slope = input('slope?\n>>> ')    # 'm'

    y_int = input('y intercept?\n>>> ') # 'b'
    
    import turtle
    graph = turtle.Turtle()
    line = turtle.Turtle()

    graph.ht()
    graph.pensize(3)
    graph.pencolor('blue')
    graph.speed(0)
    def buildgraph():
        graph.forward(1000)
        graph.backward(2000)
        graph.forward(1000)
        graph.right(90)
        graph.forward(1000)
        graph.backward(2000)

    if slope == '':
        slope = 0
        print('Undefined')
        undef = 1
        
    if y_int == '':
        y_int = 0

    slope = float(slope)
    y_int = float(y_int)



    line.ht()
    line.pensize(0)
    line.speed(0)

    buildgraph()

    line.pu()
    line.left(90)
    line.forward(y_int * 10)
    line.right(90)
    if undef == 1:
        line.pu()
    else:
        line.pd()

    if slope < 0:
        line.left(90)
        slope = slope * -1

    angle = 90 - ((90 / 2 ** (slope - 1)) / 2)
        
    line.left(angle)
    line.forward(2000)
    line.backward(4000)
graph()



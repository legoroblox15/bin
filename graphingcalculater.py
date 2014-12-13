# Graphing calculater made by legoroblox15
# Currently only works for linear functions
import turtle
def graph(m, b):
    if m == 'undefined':
        undefined = 1
    else:
        undefined = 0
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

    line.ht()
    line.pensize(0)
    line.speed(0)

    buildgraph()

    line.pu()
    if undefined == 0:
        line.left(90)
        line.forward(b * 10)
        line.right(90)
        line.pd()

        lml = abs(m)

        angle = (90 - 90 / 2 ** (lml - 1) / 2)
        if m < 0:                                      # I have to do this because of a glitch in the code, if you were using
            angle = angle * -1                    # this equation in real life it would be:
        line.left(angle)                             # m ** 0 * 90 - 90 / 2 ** (lml - 1) / 2
        line.forward(2000)                       # I hope they fix this, along with some other
        line.backward(4000)                   # mathmatical glitches, because this is very frustrating D:<
        line.forward(2000)
        line.left(angle)
        line.pu()
        line.forward(b * 10)
        line.left(90)
        line.pd()
    elif undefined == 1:
        line.forward(b * 10)
        line.left(90)
        line.pd()
        line.forward(2000)
        line.backward(4000)
        line.forward(2000)
        line.pu()
        line.right(90)
        line.backward(b * 10)
        line.pd()
def debug_test():
    graph(0, 1)
    graph(0, -1)
    graph(1, 1)
    graph(1, -1)
    graph(-1, 1)
    graph(-1, -1)
    graph('undefined', 1)
    graph('undefined', -1

import turtle
import random

def randomcolor():
    return (random.random(),random.random(),random.random())

bill = turtle.Turtle()

bill.pensize(2)
bill.speed(0)
bill.pencolor('blue')
bill.forward(100)

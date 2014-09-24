import random
import time

class Ship():
    size = None
    char = None

class PatrolBoat(Ship):
    size = 2
    char = 'P'

class Destroyer(Ship):
    size = 3
    char = 'D'

class Submarine(Ship):
    size = 3
    char = 'S'

class Battleship(Ship):
    size = 4
    char = 'B'

class AircraftCarrier(Ship):
    def __init__(self):
        self.location = None
    
    size = 5
    char = 'A'
player_carrier = AircraftCarrier()
cpu_carrier = AircraftCarrier()
#---------------------------
w = '~'

hit = '*'

miss = '@'

grid = [
    ['  ', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,],
    ['A', w, w, w, w, w, w, w, w, w],
    ['B', w, w, w, w, w, w, w, w, w],
    ['C', w, w, w, w, w, w, w, w, w],
    ['D', w, w, w, w, w, w, w, w, w],
    ['E', w, w, w, w, w, w, w, w, w],
    ['F', w, w, w, w, w, w, w, w, w],
    ['G', w, w, w, w, w, w, w, w, w],
    ['A', w, w, w, w, w, w, w, w, w],
    ['H', w, w, w, w, w, w, w, w, w],
    ['I ', w, w, w, w, w, w, w, w, w,]
]

class Board():
    for row in grid:
        for col in row:
            print(col, end = ' ')
        print('')

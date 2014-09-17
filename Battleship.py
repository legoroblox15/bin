import random
import time

class Ship():
    size = None

class PatrolBoat(Ship):
    size = 2

class Destroyer(Ship):
    size = 3

class Submarine(Ship):
    size = 3

class Battleship(Ship):
    size = 4

class AircraftCarrier(Ship):
    size = 5
#---------------------------
print('prepare for battle!')

w = '~'

hit = '*'

miss = '@'

patrol = 'P'

destroy = 'D'

submarine = 'S'

battleship = 'B'

aircraft = 'A'

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

grid[2][3] = patrol

for row in grid:
    for col in row:
        print(col, end = ' ')
    print('')



        
            
                



'''
STORY:
The satellite that used to remotely control the rover you're in was destroyed by a passing comet.

You manage to turn on a monitor with an aerial view of the place you're in (An ASCII map with: '.'s representing the lunar plains, '>' your position and 'X' the base's position), and after racking your head for a few minutes you can only remember two basic commands:

COMMANDS:
'F' to Move forward one unit
'R' to Rotate 90 degrees clockwise (to the right)

Using only these two commands can you find a way to get back to the lunar base 'X' from your Rover '>'?

IMPORTANT:
The Rover always starts looking EAST (To the right)
Astronaut protocol dictates that you FIRST move on the HORIZONTAL axis and THEN move on the VERTICAL axis

EXAMPLE:
Input:
"4 1"
"X..>"
Solution:
"R R F F F"
Rotate 180 degrees (= Rotating 90 degrees to the right twice) in order for the rover to be facing west.
Move Forward 3 times to reach the base.

'''
class Rover:
    
    def __init__(self) -> None:
        
        cols,rows = map(int,input().split())

        self.field = []
        self.index_rover = None
        self.index_objective = None
        self.movement =[]

        for row in range(rows):

            road = list(input())

            if '>' in road:
                self.index_rover = (row, road.index('>'))
            if 'X' in road:
                self.index_objective = (row, road.index('X'))
            
            self.field.append(road)

    def find_route(self):

        row, column = self.index_rover
        _row, _column = self.index_objective

        # position the rover to move horizontal first
        # the objective is at left or rigth?

        initial_rotation = False

        if (column > _column):
            self.movement = ['R', 'R']
            initial_rotation = True
        
        # if there is just one column we will just rotate once
        if (column == _column and column != 0):
            initial_rotation = True
            if (row > _row): # objetive is up
                self.movement = ['R', 'R', 'R']
            else: # objetive is down
                self.movement = ['R']
        
        # objective is in the left
        # if objetive is on the right we just need to move forward

        forward = abs(_column - column)
        
        self.movement += ['F'] * forward

        # the objetive could be up or down
        
        # objective is up (rover is down the objetive)

        if row != _row:
            if row > _row:
                if initial_rotation:
                    self.movement += ['R']
                else:
                    self.movement += ['R'] * 3

            if _row > row:
                if initial_rotation:
                    self.movement += ['R'] * 3
                else:
                    self.movement += ['R']

        forward = abs(_row - row)
        self.movement += ['F'] * forward

        return " ".join(self.movement)

def execute(debug_test = False):
    
    rover = Rover()
    route = rover.find_route()

    if debug_test:
        for entry in rover.field:
            print(entry)
        print('index_rover:', rover.index_rover)
        print('index_objetive:', rover.index_objective)
        print('route:', route)

    return route

    

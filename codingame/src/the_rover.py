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


def move(debug_test = False):
    
   
    cols,rows = map(int,input().split())
    
    field = []
    index_rover = None
    index_objective = None
    result = []

    for row,i in enumerate(range(rows)):

        road = list(input())

        if '>' in road:
            index_rover = (row, road.index('>'))
        if 'X' in road:
            index_objective = (row, road.index('X'))
        
        field.append(road)

    a,b = index_rover
    _a,_b = index_objective

    
    if b < _b:
        result = ['F'] * _b 
    
    if a < _a: # the objetive is down
        result = ['R']
        if b == _b:
            result += ['F'] * _a
    
    
    if debug_test:
        for entry in field:
            print(entry)
        print('index_rover:', index_rover)
        print('index_objetive:', index_objective)
    #print('the first map...', test_route)
    

    return ' '.join(result)
    

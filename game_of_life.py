# geometric figures ASCII
'''
for n in range(96):
     r = 9727 - n
     print(r, chr(r))

    At each step in time, the following transitions occur:

    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    
    These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

    Any live cell with two or three live neighbours survives.
    Any dead cell with three live neighbours becomes a live cell.
    All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    
'''
import random
import math
import time
import select
from os import system, sys


DEAD_CELL = ' '#chr(9633) # □
LIVE_CELL = chr(9632) # ■

class Cell:
    def __init__(self, position, limit):
    
        self.position = position
        self.set_neighbours_position(limit)
        self.neighbours = []

        if round(random.uniform(0,1)):
            self.live()
        else:
            self.die()

    def set_neighbours_position(self, limit):
        row, col = self.position
        self.neighbours_position = []

        possible_neighbor_position = {
            'up': [row - 1, col],
            'left': [row, col - 1],
            'up-left': [row - 1, col - 1],
            'down': [row + 1, col],
            'right': [row, col + 1],
            'up-right': [row - 1, col + 1],
            'down-right': [row + 1, col + 1],
            'down-left': [row + 1, col - 1]
        }
        
        for _row, _col in possible_neighbor_position.values():
            
            is_possible_row = _row >=0 and _row <= limit
            is_possible_col = _col >=0 and _col <= limit

            if is_possible_row and is_possible_col:
                self.neighbours_position.append([_row,_col])

    def set_my_neighbours(self, grid):

        for row, col in self.neighbours_position:
            self.neighbours.append(grid[row][col])

    def is_alive(self):
        return self.state == LIVE_CELL 

    def set_state(self, state):
        self.live() if state == 'live' else self.die()

    def live(self):
        self.state = LIVE_CELL
    
    def die(self):
        self.state = DEAD_CELL



class Game:
    def __init__(self, size, max_start_population = math.inf):
        self.grid = []
        self.grid_limit = size - 1
        self.max_possible_population = size * size
        self.separator = '*' * size
        self.iterations = 0
        self.live_cells = []
        self.all_cells = []
        
        for row in range(size):
            self.grid.append([])
            for col in range(size):
                position = [row,col]
                
                new_cell = Cell(position,self.grid_limit)            
                self.grid[row].append(new_cell)
                
                if len(self.live_cells) >= max_start_population:
                     new_cell.die()

                if new_cell.is_alive():
                    self.live_cells.append(new_cell)

                self.all_cells.append(new_cell)
        
        for cell in self.all_cells:
            cell.set_my_neighbours(self.grid)

    def toggle_life(self, row,col):
        cell = self.grid[row][col]

        if cell.is_alive():
            cell.die()
        else:
            cell.live()
        self.show_grid()

    def show_grid(self):
        system('clear')
        alive_cells_count = len(self.live_cells)
        print(self.separator)
        for row in self.grid:
            states = list(map(lambda cell: cell.state, row))
            print(*states)
        print(self.separator)
        print('Iterations:', self.iterations)
        print('Alive:', alive_cells_count)
        print('Dead:', self.max_possible_population - alive_cells_count)

    def big_bang(self):
        
        try:
            while True:
                    
                actions = []

                self.iterations += 1
                for row in self.grid:
                    for cell in row:
                        
                        lives = list(map(lambda c: c.is_alive(),cell.neighbours)).count(True)
                        
                        # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                        # Any live cell with more than three live neighbours dies, as if by overpopulation.    
                        next_state = 'die'
                            
                        # Any live cell with two or three live neighbours lives on to the next generation.
                        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                        if lives == 2 and cell.is_alive() or (lives == 3 and not cell.is_alive()):
                            next_state = 'live'
                        
                        #cell.set_state(next_state)
                        if next_state == 'live':
                            self.live_cells.append(cell)

                        actions.append({'cell': cell, 'next_state': next_state})
                
                
                self.live_cells = []
                for action in actions:
                        state = action['next_state']
                        cell = action['cell']

                        cell.set_state(state)
                        if state == 'live':
                            self.live_cells.append(cell)
                self.show_grid()
                time.sleep(.3)

        except KeyboardInterrupt:
            pass



def go():

    g = Game(30)

    #g.toggle_life(2,2)
    #g.toggle_life(2,3)
    #g.toggle_life(2,1)

    g.big_bang()


g = Game(40)

g.toggle_life(2,2)
g.toggle_life(2,3)
g.toggle_life(2,1)

g.big_bang()
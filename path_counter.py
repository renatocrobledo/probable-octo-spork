
'''
    Having a matrix  n x n, starting point from top-left and end bottom-right
    we want to count all the possible paths to reach the end so posible moves are right down

S  o  o  o  o
o  o  o  o  o
o  x  o  x  o
o  x  o  o  o
o  o  o  o  E


S = start
E = end
o = possible step field
x = block

'''

from collections import defaultdict

class PathCount:

    def __init__(self, board = None):
        self.dict = {}
        self.path = []
        self.board = board
        if not board:
            self.board = [
            [True, True, True, True, True],
            [False, True, False, False, True],
            [True, True, True, False, True],
            [True, False, True, False, True],
            [True, False, True, True, True]]
        
        self.last_row = len(self.board) - 1
        self.last_col = len(self.board[self.last_row]) - 1
        
        
    def valid_square(self,row,col):
        if row > self.last_row or col > self.last_col:
            return False

        return self.board[row][col]

    def is_at_end(self,row,col):
        return row == self.last_row and col == self.last_col

    def count_paths(self,row,col):
        
        print(row,col)

        if self.is_at_end(row, col):
            print('reach the end!',row,col)
            return 1
        elif not self.valid_square(row, col):
            return 0
            
        return self.count_paths(row + 1, col) + self.count_paths(row, col + 1)


p = PathCount()

print(p.count_paths(0,0))


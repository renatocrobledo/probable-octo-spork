from collections import defaultdict

import datetime

def benchmark(f):
    def inner(*args, **kwargs):

        start_time = datetime.datetime.now()
        f(*args, **kwargs)
        end_time = datetime.datetime.now()

        time_diff = (end_time - start_time)
        print(f'{f.__name__} ->', time_diff.total_seconds())
    return inner


class Hanoi:
    def __init__(self,n, print_moves=True, auto_show_board=True):

        self.print_moves = print_moves
        self.auto_show_board = auto_show_board
        self.total = n
        self.board = {
            'a': list(range(n,0,-1)),
            'b': [],
            'c': []
        }
        self.moves = 0 
        self.calls = defaultdict(list)

    def check_for_complete(self):
        
        c_len = len(self.board['c'])
        
        if c_len == self.total:
            print(f"it's complete! (having {self.total} pieces, doing {self.moves} moves)")
    
    def move(self,_from,_to):
        
        if self.print_moves:
            print(f">>> h.move('{_from}','{_to}')")

        size_from = len(self.board[_from])
    
        if size_from == 0:
            print(":( the container for extraction is empty")
            return 
        else:
            size_to = len(self.board[_to])

            piece_to_move = self.board[_from][size_from - 1] 
            
            if size_to == 0 or piece_to_move < self.board[_to][size_to - 1]:
                piece = self.board[_from].pop()
                self.board[_to].append(piece)
                self.moves += 1
                self.check_for_complete()
            else:
                print("ups, the piece you're trying to move is bigger than the one in top of the new container")
        if self.auto_show_board:
            self.show_board()
    # move from one pile to another using a helper recursively
    # f = from
    # h = helper
    # t = to
    def play(self, f='a', h='b', t='c', level=None):
        n = level
        if n == None:
            n = self.total
        
        if n == 0:
            return
        self.play(f, t, h, n - 1)
        self.move(f, t)
        self.play(h, f, t, n - 1)
    def play_memo(self, f='a', h='b', t='c', level=None):
        n = level
        if n == None:
            n = self.total
        
        cache = f'{f}{h}{t}{level}'
        
        if n == 0:
            return

        if cache in self.calls:
            f, t = self.calls[cache]
            self.move(f, t)
            return 

        self.play(f, t, h, n - 1)
        self.move(f, t)
        self.calls[cache] = [f,t]
        self.play(h, f, t, n - 1)
    

    def show_board(self):
        
        a = self.board['a']
        b = self.board['b']
        c = self.board['c']

        max_len = self.total
        divisor = '=' * (max_len * 3)
        print(divisor)
        lines = []

        for n in range(max_len - 1,-1,-1):
            
            if n < len(a):
                _a = '-' * a[n] + ' ' * (max_len - a[n])
            else:
                _a = ' ' * max_len
            
            if n < len(b):
                _b = '-' * b[n] + ' ' * (max_len - b[n])
            else:
                _b = ' ' * max_len

            if n < len(c):
                _c = '-' * c[n]
            else:
                _c = ' ' * max_len    
            
            lines.append(f'{_a}|{_b}|{_c}')
        
        print(*lines, sep='\n')
        print(divisor)

@benchmark
def play(n):
    h = Hanoi(n, print_moves=False, auto_show_board=False)
    h.play()

@benchmark
def play_memo(n):
    h = Hanoi(n, print_moves=False, auto_show_board=False)
    h.play_memo()

#play(30)
play_memo(30)
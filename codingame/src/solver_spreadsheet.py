import operator

class Solver:

    def __init__(self, n):
        self.spreadsheet = ['*'] * n
        self.ops = {
            "ADD": operator.add,
            "SUB": operator.sub,
            "MULT": operator.mul,
        }
    def show_spreadsheet(self):
        print(*self.spreadsheet, sep='\n')

    def get_value(self, id):
        if '$' in id:
            p = int(id[1:])
            if p < len(self.spreadsheet):
                return self.spreadsheet[p]
            else:
                raise Exception('ups there\'s an error in the operations I\'m trying to acces to a non-reachable index')

        return int(id)

    def solve(self, id, operation, arg_1, arg_2):

        a = self.get_value(arg_1)
        b = self.get_value(arg_2)
        result = '*'

        if a != '*' and b != '*':
            if operation == 'VALUE':
                 result = a
            else:
                op_func = self.ops[operation]
                result = op_func(a, b)
        
        self.spreadsheet[id] = result
        
        return result

n = int(input())
operations = []
solver = Solver(n)

for i in range(n):
    operation, arg_1, arg_2 = input().split()
    if operation == 'VALUE':
        operations.append([i, operation, arg_1, '0'])
    else:
        operations.append([i, operation, arg_1, arg_2])

while len(operations) > 0:
    for params in operations:
        result = solver.solve(*params)
        if result != '*':
            operations.remove(params)
            break

solver.show_spreadsheet()
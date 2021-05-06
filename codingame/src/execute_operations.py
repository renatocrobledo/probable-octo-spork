'''
    extracted from codingame, having the operation: 

    1+3*3 according to the preference operator the result will be: (3 * 3) + 1 = 10
    but applying each operator as it appears = (1+3) * 3 = 9

    so, an operation would be perfomed as the last one.

'''



operators = {
    '*': lambda a,b: a*b,
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '/': lambda a,b: a/b,
}

def evaluate_operation(op):
    
    # separate evaluation


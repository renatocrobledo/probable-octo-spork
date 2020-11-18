'''
    A closure is an inner fucntion that remembers and has access to variables in 
    the local scope in which has been created even after the outer function has finish executing
'''


def outer_fun(msg):
    message = msg
    def inner_function():
        print(message)
    return inner_function



hi_function = outer_fun('hi')
hello_function = outer_fun('hello')

hi_function() # hi
hello_function() # hello





    

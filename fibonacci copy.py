
'''
    Receiving an index (starting in one), return the value of the fibonacci secuence
    fibonacci: 1 1 2 3 5 8 13 21
    n / index: 1 2 3 4 5 6 7  8 
'''

result = {}

def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    if n in result:
        return result[n]
    else:
        result[n] = fibo(n - 1) + fibo(n - 2)    
        return result[n]


def fib_non_recursive(n):

    a, b = (0, 1) 
    for i in range(n): 
        a, b = (b, a + b) 

    return a



print(fibo(6)) # will crash at 1000
print(fib_non_recursive(6))



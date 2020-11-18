def add(n):
    
    if n == 1:
        return 1
    return n + add(n - 1)


def fib(n):
    if n == 1 or n == 0:
        return n
    
    return fib(n - 1) + fib(n - 2)

print(add(5)) # 5 + 4 + 3 + 2 + 1 = 15 

print(fib(5)) # 5
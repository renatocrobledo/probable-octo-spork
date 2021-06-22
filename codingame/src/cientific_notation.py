n = int(input())
r = "{:.2e}".format(n)
a, b = r.split('e+')

print(f'{a} * 10 ^ {int(b)}')
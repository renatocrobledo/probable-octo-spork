
n = int(input('how high? '))

pieces = []
height = n - 1
width = n + 2
for x in range(n):
    tmp = f'{" "*x}/{" " * width}\\'    
    _width = width
    
    while _width:
        _width -=2
        tmp += f'{" "*(x*2)}/{" " * _width}\\'
    pieces.append(tmp)
    width -= 2

pieces.reverse()
for p in pieces:
    print(p)
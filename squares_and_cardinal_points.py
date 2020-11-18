
'''

Search all possible sqares/rectangles that can be formed given a list of cardinals points (x, y)


So for example suppose we receive a list of points x, y : [(1,1),(1,3),(3,1),(3,3)]

which in a plot will look something like this:

  Y
3 | *   *
2 |
1 | *   *
   --------- X
    1 2 3 4


Then there is one square that is formed for the four ponts:
    1 -> [(1,1), (1,3), (3,1), (3,3)]

and if we receive:

  Y
3 | *  *  *
2 |
1 | *  *  *
   --------- X
    1 2 3 4

there will be 3 squares builded as follows:

    1 -> [(1,1), (1,3), (3,1), (3,3)]
    2 -> [(1,1), (1,3), (4,1), (4,3)] 
    3 -> [(3,1), (3,3), (4,1), (4,3)] 


This quiz was extracted from: https://www.youtube.com/watch?v=EuPSibuIKIg (Google Coding Interview With A Competitive Programmer)

'''

def search_for_squares(l):
    dx = {}
    r = 0
    for n in l:
        x, y = n
        if x in dx:
            dx[x].append(y)
        else:
            dx[x] = [y]
    r = 0
    while len(dx):
        k, v = dx.popitem()
        for _k,_v in dx.items():
            intersection = list(set(v) & set(_v))
            if len(intersection):
                r += sum(list(range(0,len(intersection)))) 
                
    return r


result = search_for_squares([(0,0),(0,2),(1,0),(1,2)])
assert  result == 1, result

result = search_for_squares([(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)])
assert  result == 3, result

result = search_for_squares([(0,1),(0,3),(1,1),(1,0),(2,5),(2,2)])
assert  result == 0, result

result = search_for_squares([(0,0),(0,2),(1,0)])
assert  result == 0, result

result = search_for_squares([(0,0),(0,2)])
assert  result == 0, result

result = search_for_squares([(0,0)])
assert  result == 0, result

result = search_for_squares([(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4)])
assert  result == 10, result

result = search_for_squares([(1,1),(1,4),(1,2),(0,0),(0,4),(0,1),(0,2),(0,3),(1,0),(1,3)])
assert  result == 10, result

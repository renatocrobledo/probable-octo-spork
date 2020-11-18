'''
 Given pairs of logic comparations return the biggest..

 for example:

 in: 
    ['a>b', 'c<a'] 
    
 out:
   'a' 
'''
from collections import defaultdict


def action_old(elements):

  e = {}

  for line in elements:

      try:
          big, small = line.split('>')
          
          b = e.get(big, 0)
          s = e.get(small, 0)
          
          if not b:
              e[big] = 0
          if not s:
              e[small] = 0
          
          e[big] += 1
          e[small] -= 1
      except:
          try:
              small, big = line.split('<')
              b = e.get(big, 0)
              s = e.get(small, 0)
              
              if not b:
                  e[big] = 0
              if not s:
                  e[small] = 0
              e[big] += 1
              e[small] -= 1
          except:
              pass

  s = [(k, e[k]) for k in sorted(e, key=e.get)]
  s.reverse()

  o = []

  for item in s:
      a,b = item
      if b > 0 :
          o.append(a)

  return " ".join(o)


def action(logic_comparations):

    dictionary = defaultdict(int)

    for l in logic_comparations:
        if '>' in l:
            bigger, smaller = l.split('>')
        else: 
            smaller, bigger = l.split('<')

        dictionary[smaller] -= 1
        dictionary[bigger] += 1


    value_bigger_than_zero = lambda o: o[1] > 0
    get_value = lambda o: o[1]

    s = filter(value_bigger_than_zero, dictionary.items())
    r = sorted(s, key=get_value, reverse=True)

    return " ".join(map(lambda o:o[0],r)) 


response = action(['A>B', 'A>C'])
assert response == 'A', response

response = action(['A>B', 'C>B', 'A>C'])
assert response == 'A', response

response = action(['A>B', 'A>C', 'E>C', 'F>C', 'F<B'])
assert response == 'A E', response

response = action(['E<C', 'F<C', 'F<B', 'Z>J', 'J<B'])
assert response == 'B C Z' or response == 'C B Z', response


def action(elements):

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

response = action(['A>B', 'A>C'])
assert response == 'A', response

response = action(['A>B', 'C>B', 'A>C'])
assert response == 'A', response

response = action(['A>B', 'A>C', 'E>C', 'F>C', 'F<B'])
assert response == 'A E', response

response = action(['E<C', 'F<C', 'F<B', 'Z>J', 'J<B'])
assert response == 'B C Z', response

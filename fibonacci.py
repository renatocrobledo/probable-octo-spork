'''
  Print a fibonacci secuence using recursion, stoping at n steps, 
  
  for example 
    
    4 steps as input:
      1 1 2 3 5 8
    
    10 steps:
    1 1 2 3 5 8 13 21 34 55 89 144
  
'''

def get_args(args): 
   a = args.get('a',1)
   b = args.get('b',1)
   result = args.get('result',[])
   count = args.get('count',2)
   return a, b, result, count

# return a list with "n" fibonacci elements
def get_fibonacci_list(steps, args = {}):
    a, b, result, count = get_args(args)
    result.append(str(a))
    if count == steps:
      result.append(str(b))
      return result
    else:
      params = {
          'a': b,
          'b': a + b,
          'result': result,
          'count': count + 1
      }
      return get_fibonacci_list(steps, params)

# fibonacci value at "n" position starting by zero
def get_fibonacci_at_position(n):
  if n == 0 or n == 1:
     return 1
  else:
     return get_fibonacci_at_position(n - 1) + get_fibonacci_at_position(n - 2)


def get_fibonacci_at_position_non_recursive(n):
  a = 1
  b = 1
  for i in range(2, n + 1):
    a, b = b, a + b
  return b

def test():
  
  result = get_fibonacci_at_position(5)
  assert result == 8, result

  result = get_fibonacci_at_position(11)
  assert result == 144, result

  result = get_fibonacci_at_position_non_recursive(5)
  assert result == 8, result

  result = get_fibonacci_at_position_non_recursive(11)
  assert result == 144, result

  result = get_fibonacci_list(6)
  assert result == ['1', '1', '2', '3', '5', '8'], result

  result = get_fibonacci_list(12)
  assert result == ['1', '1', '2', '3', '5', '8', '13', '21', '34', '55', '89', '144'], result

test()
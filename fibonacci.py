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
   count = args.get('count',0)
   return a, b, result, count

def fibonacci(steps, args = {}):
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
      return fibonacci(steps, params)

def test():
  
  result = fibonacci(4)
  assert result == ['1', '1', '2', '3', '5', '8'], result

  result = fibonacci(10)
  assert result == ['1', '1', '2', '3', '5', '8', '13', '21', '34', '55', '89', '144'], result

test()
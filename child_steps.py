'''
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs
'''
# Brute force

'''
the runtime of this algorithm is exponential (roughly O (3^n) ), since each call
branches out to three more calls
'''

def count_ways(n):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  else:
    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3) 


result = count_ways(3)
assert result == 4, result


'''
using 'cache' Memoization:

'''

mem = {} 

def count_ways_memo(n):
  if n < 0:
    return 0
  elif n == 0:
    return 1
  if n in mem:
    return mem[n]
  else:
    mem[n] = count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3) 
    return mem[n]


result = count_ways_memo(3)
assert result == 4, result

'''
note that the number of ways will quickly overflow the bounds of an integer. 
By the time you get to just n 37, the result has already overflowed

'''
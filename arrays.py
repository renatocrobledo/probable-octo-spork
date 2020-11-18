from array import array 
import numpy as np

#a = array('i',[1,2,3,4,5,6]) # initializing an integer array
#print(a) # array('i', [1, 2, 3, 4, 5, 6])

a = np.array([1,2,3,4,5,6])

result = a * 3 # multiply all elements by 3

print(result) #  [ 3  6  9 12 15 18]


b = np.array(['a','b','c','d'])

r = b + 'z'

print(r)



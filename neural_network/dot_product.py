import numpy as np

# 4 * 2 matrix Rows * columns
a = [[1,0],[0,1],[0,2],[0,3]]

# 2 * 3
b = [[4,1,3],[2,2,3]]

# result 4 * 3
c = np.dot(a,b)

print(c)

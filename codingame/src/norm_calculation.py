'''
You are given an integer matrix of size N * M (a matrix is a 2D array of numbers).

A norm is a positive value meant to quantify the "size/length" of an element. In our case we want to compute the norm of a matrix.
There exist several norms, used for different scenarios.

Some of the most common matrix norms are :
- The norm 1: for each column of the matrix, compute the sum of the absolute values of every element in that column. The norm 1 is the maximum of these sums.
- The infinite norm: for each row of the matrix, compute the sum of the absolute values of every element in that row. The infinite norm is the maximum of these sums.
- The max norm: compute the maximum of the absolute values of every element in the matrix.

Given the matrix, print these three norms.
Input
N the number of rows
M the number of columns
Next N lines: the M values of each element in the row of the matrix
Output
A single line: N_1 N_INF N_MAX
With :
N_1 the norm 1 of the matrix
N_INF the infinite norm of the matrix
N_MAX the max norm of the matrix


'''


# transpose 2D list in Python (swap rows and columns)


n = int(input())
m = int(input())

l = []
whole_max = 0
rows = []
for i in range(n):
    row = list(map(lambda x: abs(int(x)),input().split()))
    _max = max(row)

    if _max > whole_max:
        whole_max = _max
    rows.append(sum(row))
    l.append(row)

cols = []
for t in list(zip(*l)):
    cols.append(sum(t))

norm_1 = max(cols)
infinite_norm = max(rows)
max_norm = whole_max

print(f'{norm_1} {infinite_norm} {max_norm}')
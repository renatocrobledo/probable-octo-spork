'''
  Giving a matrix of N X M values, build a function that takes that matrix as input and print its values folowing a spiral, so for example:
  
  Receiving this 4 X 4 matrix as imnut:
    
    1 2 3
    4 5 6
    7 8 9

  It is expected to get the following output:

    1 2 3
    8 9 4
    7 6 5

  Another examples:

  input:

    1  2  3  4
    5  6  7  8
    9  10 11 12
    13 14 15 16
  
  output:
    
    1   2  3  4
    12  13 14 5
    11  16 15 6
    10  9  8  7
'''



l_1 = [ 
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]

l_1_r = [  
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
]


l_2 = [ 
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
]

l_2_r = [  
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
]


l_3 = [ 
        [1, 2, 3],
        [4, 5, 6],
]

l_3_r = [  
        [1, 2, 3],
        [6, 5, 4],
]



l_4= [ 
        [1, 2, 3, 4, 5, 6, 7],

]

l_4_r = [  
        [1, 2, 3, 4, 5, 6, 7],
]


l_5 = [ 
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
]

l_5_r = [ 
        [1, 2],
        [8, 3],
        [7, 4],
        [6, 5],
]

l_7 = [
      [1, 2, 3, 4, 5, 6, 7, 8, 9],
      [10, 11, 12, 13, 14, 15, 16, 17, 18],
      [19, 20, 21, 22, 23, 24, 25, 26, 27],
      [28, 29, 30, 31, 32, 33, 34, 35, 36],
      [37, 38, 39, 40, 41, 42, 43, 44, 45], 
      [46, 47, 48, 49, 50, 51, 52, 53, 54], 
      [55, 56, 57, 58, 59, 60, 61, 62, 63], 
      [64, 65, 66, 67, 68, 69, 70, 71, 72],
      [73, 74, 75, 76, 77, 78, 79, 80, 81]
]

l_7_r = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9], 
  [32, 33, 34, 35, 36, 37, 38, 39, 10], 
  [31, 56, 57, 58, 59, 60, 61, 40, 11], 
  [30, 55, 72, 73, 74, 75, 62, 41, 12], 
  [29, 54, 71, 80, 81, 76, 63, 42, 13], 
  [28, 53, 70, 79, 78, 77, 64, 43, 14], 
  [27, 52, 69, 68, 67, 66, 65, 44, 15], 
  [26, 51, 50, 49, 48, 47, 46, 45, 16], 
  [25, 24, 23, 22, 21, 20, 19, 18, 17]]

def get_stream_list(l):
  stream = []
  for row in l:
    for col in row:
      stream.append(col)
  return stream


def make_spiral(l):

  my_list = get_stream_list(l)
  
  rows = len(l)
  cols = len(l[0])
  
  tmp_dict = {}
  
  total_elements = rows * cols

  # limits:
  right = cols
  left = 0
  down = rows
  up = 1

  row = 0
  col = 0
  focus = 0

  while 0 <= focus < total_elements:
    
    try:
      while col < right:
        tmp_dict[f'{row}_{col}'] = my_list[focus]
        col += 1
        focus += 1
      col -= 1
      focus -= 1

      while row < down:
        tmp_dict[f'{row}_{col}'] = my_list[focus]
        row += 1
        focus += 1
      row -= 1
      focus -= 1

      while col >= left:
        tmp_dict[f'{row}_{col}'] = my_list[focus]
        col -= 1
        focus += 1
      col += 1
      focus -= 1

      while row >= up:
        tmp_dict[f'{row}_{col}'] = my_list[focus]
        row -= 1
        focus += 1
      row += 1
      focus -= 1


      right -= 1
      left += 1
      down -= 1
      up += 1
    except IndexError:
      focus = total_elements

  
  result = []

  for r in range(rows):
    list_row = []
    for c in range(cols):
      list_row.append(tmp_dict[f'{r}_{c}'])
    result.append(list_row)

  print(my_list, "-->", get_stream_list(result))

  return result


assert make_spiral(l_1) == l_1_r, "ups, wrong result l_1"
assert make_spiral(l_2) == l_2_r, "ups, wrong result l_2"
assert make_spiral(l_3) == l_3_r, "ups, wrong result l_3"
assert make_spiral(l_4) == l_4_r, "ups, wrong result l_4"
assert make_spiral(l_5) == l_5_r, "ups, wrong result l_5"
assert make_spiral(l_7) == l_7_r, "ups, wrong result l_7"
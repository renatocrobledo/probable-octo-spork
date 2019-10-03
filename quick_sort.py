

def partition(array, left, right, pivot):
  while left <= right:

      while array[left] < pivot:
        left += 1
    
      while array[right] > pivot:
        right -= 1

      if left <= right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

  return left

def quick_sort_mutation(array, left, right):

    if left >= right:
      return

    pivot_index = int((left + right) /2)
    pivot = array[pivot_index]

    main_index = partition(array, left, right, pivot)

    quick_sort_mutation(array, left, main_index - 1)
    quick_sort_mutation(array, main_index, right)


def quick_sort(array):

  if len(array) == 0:
    return []
  
  left = []
  right = []
  pivot = array[0]

  for element in array:
    if element == pivot:
      continue
    if element < pivot:
      left.append(element)
    else:
      right.append(element)
  
  return quick_sort(left) + [pivot] + quick_sort(right)
  
def test():
  
  A = [6, 3, 17, 11, 4, 44, 76, 23, 12, 30]
  result = quick_sort(A) 
  assert result == [3, 4, 6, 11, 12, 17, 23, 30, 44, 76], result

  A = [1,1,1,1,0,0,0,0]
  result = quick_sort(A) 
  assert result == [0,1], result


  B = [6, 3, 17, 11, 4, 44, 76, 23, 12, 30]
  quick_sort_mutation(B, 0, len(B) - 1)
  assert B == [3, 4, 6, 11, 12, 17, 23, 30, 44, 76], B

  B = [1,1,1,1,0,0,0,0]
  result = quick_sort(B) 
  assert result == [0,1], result

test()
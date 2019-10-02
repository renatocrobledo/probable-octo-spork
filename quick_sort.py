'''
// Create an array to sort
var array = [9, 2, 5, 6, 4, 3, 7, 10, 1, 12, 8, 11];

// Basic implementation (pivot is the first element of the array)
function quicksort(array) {
    if (array.length == 0) return [];

    var left = [], right = [], pivot = array[0];

    for (var i = 1; i < array.length; i++) {
        if(array[i] < pivot)
            left.push(array[i])
        else
            right.push(array[i]);
    }

    return quicksort(left).concat(pivot, quicksort(right));
}

console.log(quicksort(array.slice())); // => [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]

'''

def quick_sort_mutation(array, left, right):
    
    pivot_index = int((left + right) /2)

    while left <= right:

      while array[left] < array[pivot_index]:
        left += 1
    
      while array[right] > array[pivot_index]:
        right -= 1

      if array[left] > array[right]:
        array[left], array[right] = array[right], array[left]

    quick_sort_mutation(array, 0, pivot_index)
    quick_sort_mutation(array, pivot_index, len(array) - 1)



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
  result = quick_sort(A) #(the list, the index of the first element of the list, the index of the pivot)
  assert result == [3, 4, 6, 11, 12, 17, 23, 30, 44, 76], result

  B = [6, 3, 17, 11, 4, 44, 76, 23, 12, 30]
  quick_sort_mutation(B, 0, len(B) - 1)
  assert B == [3, 4, 6, 11, 12, 17, 23, 30, 44, 76], B



test()
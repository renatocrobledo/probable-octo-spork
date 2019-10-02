

'''
  Giving a list composed by zeroes and ones, print the count of chunks of ones:

  Example:

    input: [0,0,1,0,1,1,1,0,0,1,1,0,1]
    output: 4
      because there are:
        * one number one at position 2
        * three ones from position 4 to 6
        * two ones from position 9 to 10 
        * one at the end of the list

'''

def count_chunks_of_ones(array):
  str_elements_list = [ str(i) for i in array ]
  str_text = "".join(str_elements_list)
  # separate by zeros and remove empty
  filtered_list = list(filter(None, str_text.split("0"))) 
  return len(filtered_list)


def test():
  l = [0,0,1,0,1,1,1,0,0,1,1,0,1]
  assert count_chunks_of_ones(l) == 4, 'ups, should be four'
  l = [0,1,0,1,0,1,1]
  assert count_chunks_of_ones(l) == 3, 'ups, should be four'
  l = [0,0,1,0,0,0,0,0,0,0,0,1]
  assert count_chunks_of_ones(l) == 2, 'ups, should be two'
  l = [0,0,0,0,1,0,0,0,0,0,0,0]
  assert count_chunks_of_ones(l) == 1, 'ups, should be one'
  l = [0,0,0,0,0,0,0,0,0,0,0,0]
  assert count_chunks_of_ones(l) == 0, 'ups, should be zero'
  l = []
  assert count_chunks_of_ones(l) == 0, 'ups, should be zero'
  l = [0]
  assert count_chunks_of_ones(l) == 0, 'ups, should be zero'
  l = [1]
  assert count_chunks_of_ones(l) == 1, 'ups, should be one'
  l = [1,1,1,1,1,1,1,1]
  assert count_chunks_of_ones(l) == 1, 'ups, should be one'
  
  return "Alright"

test()

def each_element_to_str(l):
  return list(map(str, l))


def test():
  a = [1,2,3,4,5,6,7,8,9]
  result = each_element_to_str(a)
  assert result == ['1', '2', '3', '4', '5', '6', '7', '8', '9'], result

test()

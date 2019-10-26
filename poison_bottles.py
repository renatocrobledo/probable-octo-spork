'''
You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips which
can be used to detect poison. A single drop of poison will turn the test strip positive permanently.
You can put any number of drops on a test strip at once and you can reuse a test strip as many times
as you'd like (as long as the results are negative). However, you can only run tests once per day and
it takes seven days to return a result. How would you figure out the poisoned bottle in as few days
as possible? 

'''

import random
MAX_TEST_STRIPES = 10
TOTAL_BOTTLES = 1000

class Bottle:
  def __init__(self, _id):
    self.poisoned = False  
    self.id = _id
  
  def __repr__(self):
    if self.poisoned: 
      return 'X'
    else:
      return '0'
  
  def is_poisoned(self):
    return self.poisoned

  def set_poisoned(self):
    self.poisoned = True

class SodaBatch:
  def __init__(self):
    self.bottles = []
    for i in range(TOTAL_BOTTLES):
      self.bottles.append(Bottle(i))

    poisoned_bottle_position = random.randrange(TOTAL_BOTTLES - 1)
    poisoned_bottle = self.bottles[poisoned_bottle_position]

    poisoned_bottle.set_poisoned()
  

class Tester:
  def __init__(self):
      self.test_stripes = MAX_TEST_STRIPES
      self.days_passed = 0

  def is_there_a_poisoned_bottle(self, bottles):
    for b in bottles:
      if b.is_poisoned():
        self.test_stripes -= 1
        self.days_passed += 7
        return True
    return False

  def get_positive_test(self, bottles):
      bottles_quantity = len(bottles)

      chunk = int(bottles_quantity / self.test_stripes) or 1

      for i in range(0, len(bottles), chunk):
          batch_to_test = bottles[i:i + chunk]
          if self.is_there_a_poisoned_bottle(batch_to_test):
            return batch_to_test
      

def run_test(soda):

  bottles = soda.bottles
  tester = Tester()

  tmp_test = tester.get_positive_test(bottles)

  while len(tmp_test) > 1:
    tmp_test = tester.get_positive_test(tmp_test)

  poisoned_bottle = tmp_test[0]
  
  print('The poisoned bottle was found in the position:', poisoned_bottle.id)
  print(tester.days_passed, 'days passed')
  print(MAX_TEST_STRIPES - tester.test_stripes, 'test stripes used')

run_test(SodaBatch())

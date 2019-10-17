'''

Queue implements the FIFO 


Basic operations of Queue
Enqueue() — Inserts element to the end of the queue
Dequeue() — Removes an element from the start of the queue
isEmpty() — Returns true if queue is empty
Top() — Returns the first element of the queue



Reverse first k elements of a queue
'''

class Queue:
  def __init__(self):
    self.container = []

  def enqueue(self, value):
    self.container.append(value)
  
  def dequeue(self):
    if self.is_empty():
      return Exception('ups, the queue is empty')

    return self.container.pop(0)
  
  def is_empty(self):
    # Returns true if queue is empty
    return not bool(len(self.container))

  def top(self):
    if self.is_empty():
      return Exception('ups, the queue is empty')
    
    return self.container[0]

  def reverse_first_n_elements(self, n):
    
    tmp_list = self.container[:n]
    tmp_list.reverse()

    self.container = tmp_list + self.container[n:]

  # Generate binary numbers from 1 to n using a queue  
  def generate_binary_up_to(self, n):
    
    for i in range(n):
      current_value = i + 1
      # transform to binary and removes the '0b' character at the beginning
      binary = str(bin(current_value))[2:]
      self.enqueue(binary) 
      

def test():

  q = Queue()
  q.container = [1,2,3,4,5,6,7,8,9]
  q.reverse_first_n_elements(3)

  assert q.container == [3, 2, 1, 4, 5, 6, 7, 8, 9], q.container

  q = Queue()
  q.generate_binary_up_to(10)
  
  assert q.container == ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010'], q.container


test()
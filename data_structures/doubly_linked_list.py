class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self):
    self.root = None
  
  def print(self):
    
    actual_node = self.root
    result = []
    while actual_node.next and actual_node.next != self.root:
      result.append(actual_node.value)
      actual_node = actual_node.next
    
    linked_list_str = '<->'.join(result)
    print(linked_list_str)
    return linked_list_str

  def insert_in_empty_list(self, value):
    if self.root == None:
      self.root = Node(value)
    else 
      raise Exception('Ups, the list is not empty')

  def insert_at_front(self, value):
    
    try:
      self.insert_in_empty_list(value)
    except Exception:
      new_node = Node(value)
      new_node.next = self.root
      new_node.prev = self.root
      self.root.next = new_node
      self.root.prev = new_node

def test():

  doubly_list = DoublyLinkedList()

  doubly_list.insert_at_front('A')
  doubly_list.insert_at_front('B')
  
  result = doubly_list.print()
  assert result == 'B<->A', result


test()
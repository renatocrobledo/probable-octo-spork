
class Node:
  def __init__(self, value):
    self.value = value
    self.ref = None

class LinkedList:
  def __init__(self):
    self.head = None

  # traverse
  def traverse(self):
    
    if self.head == None:
      return Exception("ups, the list is empty")

    current_node = self.head

    node_values = []
    while current_node != None:
      node_values.append(str(current_node.value))
      current_node = current_node.ref

    return "->".join(node_values) 

  # insert at the beginnig
  def insert_at_beginning(self, value):

    new_head = Node(value)
    
    if not self.head:
      self.head = new_head
    else:
      new_head.ref = self.head
      self.head = new_head
  
  # instert at the end
  def insert_at_end(self, value):
    new_end = Node(value)
    
    if not self.head:
      self.head = new_end
      return

    current_node = self.head

    while current_node.ref != None:
      current_node = current_node.ref

    current_node.ref = new_end


def test():

  l = LinkedList()
  l.insert_at_beginning(5)
  l.insert_at_beginning(2)
  l.insert_at_end(7)
  l.insert_at_end(8)
  l.insert_at_end(9)

  result = l.traverse()
  print(result)
  assert result == "2->5->7->8->9", result


test()
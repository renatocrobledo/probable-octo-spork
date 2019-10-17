class Node:
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None
  
class BinaryTree:
  def __init__(self, value):
    self.root = Node(value)

  def insert(self, value, node = None):
    if not node:
       node = self.root

    if value <= node.value:
      if not node.left:
        node.left = Node(value)
      else :
        self.insert(value, node.left) 
    else:
      if not node.right:
        node.right = Node(value)
      else:
        self.insert(value, node.right) 
    
  def print(self, traversal_type):
    try:
      traversal_function = getattr(self, f'{traversal_type}_print')
      print(traversal_type, traversal_function(self.root, ""))
    except Exception as e:
      print("ups :( ", e)

  def pretty_print(self, node, level):        
    counter = self.recursively_print(node, 0, {})
    height = len(counter.keys()) - 1

    for k,v in counter.items():
          tmp_list = list(map(str,v))
          tab = "  " * (height - int(k))
          print(tab, "  ".join(tmp_list))
          rows_conector = ""
          if height == k:
            continue
          for n in tmp_list:
            rows_conector += "/ \\ "
          print(tab, rows_conector)
    

  def recursively_print(self, node, level, counter):
    if node:
      if not counter.get(level):
        counter[level] = []
      counter[level].append(node.value)

      counter = self.recursively_print(node.left, level + 1, counter)
      counter = self.recursively_print(node.right, level + 1, counter)
    return counter
  

  def preorder_print(self, node, traversal):
    # Root -> Left -> right
    if node:
      traversal += f'{str(node.value)} - '
      traversal = self.preorder_print(node.left, traversal)
      traversal = self.preorder_print(node.right, traversal)
    return traversal

  def inorder_print(self, node, traversal):
    # Left -> Root -> Right
    if node:
      traversal = self.inorder_print(node.left, traversal)
      traversal += f'{str(node.value)} - '
      traversal = self.inorder_print(node.right, traversal)
    return traversal

  def postorder_print(self, node, traversal):
    # Left ->  Right -> Root
    if node:
      traversal = self.postorder_print(node.left, traversal)
      traversal = self.postorder_print(node.right, traversal)
      traversal += f'{str(node.value)} - '
    return traversal


tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(8)
tree.insert(4)
tree.insert(14)
tree.insert(16)

tree.print("pretty")
'''
tree.print("inorder")
tree.print("preorder")
tree.print("postorder")
'''
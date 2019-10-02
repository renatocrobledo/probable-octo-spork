class Node:
 def __init__(self, value):
   self.value = value
   self.right = None
   self.left = None

class BinaryTree:
 def __init__(self, root):
   self.root = Node(root)
 
 def print_tree(self, trversal_type):
   try:
     traversal_function = getattr(self, f'{trversal_type}_print')
     print(traversal_function(self.root, ""))
   except Exception as e:
     print("ups :( ", e)
 
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
 
 
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
 
#           1
#        /     \
#       2       3
#     /   \    /  \
#   4      5  6    7
 
# PRE - order:
 
#   1) check if the current node is empty or null
#   2) Display the current Node
#   3) Traverse the left subtree by recursively calling the pre-order function
#   4) Traverse the right subtree by recursively calling the pre-order function 
# tree.print_tree('preorder') # 1 - 2 - 4 - 5 - 3 - 6 - 7
 
# IN - order:
 
#   1) check if the current node is empty or null
#   2) Traverse the left subtree by recursively calling the in-order function
#   3) Display the current Node
#   4) Traverse the right subtree by recursively calling the in-order function
 
# tree.print_tree('inorder') # 4 - 2 - 5 - 1 - 6 - 3 - 7
 
 
 
# POST - order:
 
#   1) check if the current node is empty or null
#   2) Traverse the left subtree by recursively calling the post - order function
#   3) Traverse the right subtree by recursively calling the post - order function
#   4)  Display the current Node
 
# tree.print_tree('postorder') # 4 - 5 - 2 - 6 - 7 - 3 - 1

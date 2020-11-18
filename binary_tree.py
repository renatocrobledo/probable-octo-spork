class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self, root_data):
        self.root = Node(root_data)
        
    def extract_str(self, node):
        
        if node == None:
            return ''
        
        return f'{self.extract_str(node.left)},{node.data},{self.extract_str(node.right)}' 


    def __str__(self) -> str:
        return self.extract_str(self.root)


    def print_parents(self, node, value):
        
        if node == None:
            return False

        if  node.value == value:
            return True


        if self.print_parents(node.left, value) or self.print_parents(node.right, value):
            print(node.value)
            return True

        return False


tree = Tree(65)
tree.root.right = Node(70)
tree.root.left = Node(45)
tree.root.left.right = Node(40)
tree.root.left.left = Node(30)
tree.root.left.left.left = Node(20)
tree.root.left.left.right = Node(35)

#tree.print_parents(tree.root, 40) # 45 65

tree.print_parents(tree.root, 35) # 30 45 65
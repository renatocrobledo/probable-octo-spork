'''

Huffman Coding is an algorithm for doing data compression and it forms the basic idea behind file compression. Instead of allowing every character to occupy 8 bits in a file, we use variable-length encoding to assign each symbol a unique binary code according to the frequency of the character in the file, without any ambiguities.

To put this into perspective: Suppose a file contains a string “aabacdeade”, where frequency of characters a, b, c, d and e is 4, 1, 1, 2 and 2 respectively. We assign binary codes to each character as follows:
a --> 00	  b --> 010	  c --> 011	  d--> 10	  e--> 11 

The process of encoding can be divided into two parts:

Part 1: Building a Huffman tree
First, assume all of the characters as individual trees with frequency as their weight. Now, we use a greedy approach to find the two trees with the smallest weights. Then, join them to create a new tree with the sum of those two as its weight and repeat this process until we have a single tree remaining.

For the above example:

Step 1:   [a] [d] [e]    #      --> Here: a = 4, d = 2, e = 2, (bc) = 2
                        / \
                      [b] [c]

Step 2:   [a]    #          #      --> Here: a = 4, (bc) = 2, (de) = 4
                / \        / \
              [b] [c]    [d] [e]

Step 3:       #            #      --> Here: (de) = 4, (a(bc)) = 6
             / \          / \
           [a]  #       [d] [e]
               / \
             [b] [c]

Step 4:        #             --> Here: ((de)(a(bc))) = 10
              / \   
             /   \  
            /     \   
           #       #  
          / \     / \
       [a]   #  [d] [e]
            / \
          [b] [c]


Part 2: Assigning binary codes to each symbol by traversing Huffman tree
Generally, bit ‘0’ represents the left child and bit ‘1’
represents the right child

                   #                          
                0 / \ 1  
                 /   \  
                /     \
               /       \
              #         #
           0 / \ 1   0 / \ 1
            /   \     /   \
         [a]     #  [d]   [e]
              0 / \ 1
               /   \
             [b]   [c]

Thus by going through the tree, we will come up with
a = 00, b = 010, c = 011, d = 10, e = 11

'''
import math
from collections import defaultdict

class Node:
    def __init__(self, value = None, left = None, right = None, index = None):
        
        self.value = value
        self.left = left
        self.right = right
        self.index = index
        self.parent = None

    def __repr__(self) -> str:
        return str(self.value)

class Huffman:

    def __init__(self, weights):
        
        roots = []
        self.tree = None
        self.structure = defaultdict(list)
        tmp_roots = []

        for index, weight in enumerate(weights):
            roots.append(Node(weight, None, None, index))

        self.leaves = roots.copy()

        while len(roots):# or len(tmp_roots):
            '''
            if len(tmp_roots) and not len(roots):
                roots = tmp_roots.copy()
                tmp_roots = []
            elif not len(tmp_roots) and not len(roots):
                break
            '''
            a = min(roots, key=lambda o: o.value)
            roots.remove(a)
            self.tree = a
            
            if len(roots):

                b = min(roots, key=lambda o: o.value)
                roots.remove(b)
                value = a.value + b.value

                if a.value < b.value:
                    new_node = Node(value,a,b)    
                else:
                    new_node = Node(value,b,a)

                a.parent = new_node
                b.parent = new_node
                roots.append(new_node)


    def recursive_encoding(self, sub_tree, l, value = ''):
        
        if sub_tree.index != None:
            l.append(value)
            return value[:-1]
        
        self.recursive_encoding(sub_tree.left, l, value + '0')
        self.recursive_encoding(sub_tree.right, l, value + '1')

        return value[:-1]

    def encode(self):
        l = []
        self.recursive_encoding(self.tree, l)
        return l

    def build_structure(self, sub_tree, level, structure):
        
        if sub_tree == None:
            return level-1

        if sub_tree != None:
            parent = ['']
            if sub_tree.parent:
                _parent = sub_tree.parent
                parent = []
                while _parent:
                    parent.append(str(_parent.value))
                    _parent = _parent.parent
                parent.append('root')
                parent.reverse()

                
            self.structure[level].append({ 'value': sub_tree.value, 'index': sub_tree.index, 'path': "->".join(parent)})

        self.build_structure(sub_tree.left, level + 1, structure)
        self.build_structure(sub_tree.right, level + 1, structure)

        return level
        
    def print_structure(self):
        root = ''
        for key, values in self.structure.items():
            values = list(filter(lambda o: o['index'] != None, values))
            nodes = map(lambda o: f'{o["path"]}->{o["value"]}', values) 
            print(*nodes,sep='\n')
            
def play():

    n = int(input())
    weights = []
    for i in input().split():
        weights.append(int(i))

    h = Huffman(weights)
    h.build_structure(h.tree, 0, h.structure)

    h.print_structure()


    #binary_encode = h.encode()
    paths = []
    for leave in h.leaves:
        path = ''
        _inner = leave.parent
        
        while _inner != None:
            path += 'x'
            _inner = _inner.parent
        paths.append(path)
    
    #paths.reverse()

    count = 0
    for index, code in enumerate(paths):

        size = len(code) or 1

        count += (weights[index] * size)

    return str(count)



#play()
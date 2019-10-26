'''

https://www.youtube.com/watch?v=TIbUeeksXcI

Depth First search - DFS > Going deep

* Stack (LIFO), culd be own stack or trhough recursion



Breadt Firt search - BFS > Going Wide

* Queue (FIFO), iterative with a queue

'''



class Graph:

  def __init__(self, graph):
    self.graph = graph


  def dfs(node_start):
    pass



graph = {
  'A': ['B', 'G'],
  'B': ['A', 'C', 'D'],
  'C': ['B', 'D', 'E', 'F'],
  'D': ['B', 'C', 'E'],
  'E': ['C', 'D', 'F', 'H'],
  'F': ['C', 'E', 'G'],
  'G': ['A', 'F', 'H']
}

# nice xplanation: https://www.youtube.com/watch?v=TIbUeeksXcI

from collections import defaultdict


class Graph:

  def __init__(self, graph = None):
    self.graph = defaultdict(list)
    self.visited = []

    if graph:
      for node in graph:
        for connection in graph[node]:
          self.add_edge(node, connection)

  def add_edge(self, node, connection):
    self.graph[node].append(connection)
  
  # Depth First search - DFS > Going deep
  # Stack (LIFO), culd be own stack or through recursion
  def dfs(self, current_node, visited = None):

    if not visited:
      visited = set()
      self.visited = []
    
    visited.add(current_node)

    self.visited.append(current_node)

    for n in self.graph[current_node]:
      if not n in visited:
        self.dfs(n,visited)

  # Breadt Firt search - BFS > Going Wide
  # Queue (FIFO), iterative with a queue
  def bfs(self, root):
    
    visited = set([root])
    self.visited = []
    queue = list(visited)

    while queue:
      
      node = queue.pop(0)
      self.visited.append(node)

      for n in self.graph[node]:
        if n not in visited:
          queue.append(n)
          visited.add(n)

def test_graph_building():
  TEST_GRAPH = {
    'A': ['B', 'G'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D', 'E', 'F'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D', 'F', 'H'],
    'F': ['C', 'E', 'G'],
    'G': ['A', 'F', 'H']
  }
  g = Graph(TEST_GRAPH)
  graph = dict(g.graph)
  assert dict(graph) == TEST_GRAPH, graph

def test_dfs():
  
  g = Graph()
  g.add_edge(0, 1) 
  g.add_edge(0, 2) 
  g.add_edge(1, 2) 
  g.add_edge(2, 0) 
  g.add_edge(2, 3) 
  g.add_edge(3, 3)
  
  g.dfs(2)

  assert g.visited == [2,0,1,3], g.visited

  g = Graph({
    'A': ['B', 'C'],
    'B': ['A','D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['B', 'D', 'F'],
    'F': ['D', 'E']
  })

  g.dfs('A')

  assert g.visited == ['A','B','D','E','F','C'], g.visited

  g = Graph({
    0: [1, 2, 3],
    1: [],
    2: [4],
    3: [],
    4: []
  })
  g.dfs(0)

  assert g.visited == [0,1,2,4,3], g.visited


  g = Graph({
    0: [1,3],
    1: [2],
    2: [],
    3: []
  })
  g.dfs(0)

  assert g.visited == [0,1,2,3], g.visited



def test_bfs():
  
  TEST_GRAPH_1 = {
    'A': ['B', 'C'],
    'B': ['A','D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['B', 'D', 'F'],
    'F': ['D', 'E']
  }

  g = Graph(TEST_GRAPH_1)
  g.bfs('A')

  assert g.visited == ['A','B','C','D','E','F'], g.visited

  # ====================================== 

  g = Graph() 
  g.add_edge(0, 1) 
  g.add_edge(0, 2) 
  g.add_edge(1, 2) 
  g.add_edge(2, 0) 
  g.add_edge(2, 3) 
  g.add_edge(3, 3) 

  g.bfs(2)
  
  assert g.visited == [2,0,3,1], g.visited






test_graph_building()
test_dfs()
test_bfs()






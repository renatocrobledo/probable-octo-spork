
class Graph:
  def __init__(self, graph_dict = None):
    
    if graph_dict == None:
       graph_dict = {}
    
    self.graph_dict = graph_dict

  def generate_edges(self):
    
    edges = []
    for node in self.graph_dict:
      for element in self.graph_dict[node]:
        edges.append((node, element))
    return edges

  def get_isolated_nodes(self):
    
    isolated = []

    for node in self.graph_dict:
      if not self.graph_dict[node]:
        isolated.append(node)
    return isolated

  def get_vertices(self):
    return list(self.graph_dict.keys())



def test():

  g = {
    'a': ['c', 'd'],
    'b': ['c'],
    'c': ['a','d', 'f','g'],
    'd': ['a'],
    'e': [],
    'f': ['c'],
    'g': ['c'],
    'h': []
  }

  graph = Graph(g)
  edges = graph.generate_edges()

  assert edges == [('a', 'c'), ('a', 'd'), ('b', 'c'), ('c', 'a'), ('c', 'd'), ('c', 'f'), ('c', 'g'), ('d', 'a'), ('f', 'c'), ('g', 'c')], edges

  isolated = graph.get_isolated_nodes()
  
  assert isolated == ['e', 'h'], isolated

  vertices = graph.get_vertices()

  assert vertices == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], vertices

test()
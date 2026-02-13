# ---------- GRAPH STRUCTURE ---------- #

# Define the Node class
class Node:
  def __init__(self, id, x, y):
    self.id = id
    self.x = x
    self.y = y
  
  
# Define the Graph class
class Graph:
  def __init__(self):
    self.nodes = {}
    self.edges = {}
    self.cost = {}

  # Add node and edge function
  def add_node(self, id, x, y):
    self.nodes[id] = Node(id, x, y)
    if id not in self.edges:
      self.edges[id] = []

  # Add edge with cost 
  def add_edge(self, a, b, cost):
    if a not in self.edges:
      self.edges[a] = []
    self.edges[a].append(b)
    self.edges[a].sort()
    self.cost[(a, b)] = cost
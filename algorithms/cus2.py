# IDA* - Iterative Deepening A
import math

# ---------- DATA STRUCTURE ---------- #

# Define the Node class
class Node:
  def __init__(self, id, x, y):
    self.id = id
    self.x = x
    self.y = y
  
  
# Define the Graph class
class Graph:
  def __init__(self):
    # Define the node position
    self.nodes = {
      1: Node(1, 4, 1),
      2: Node(2, 2, 2),
      3: Node(3, 4, 4),
      4: Node(4, 6, 3),
      5: Node(5, 5, 6),
      6: Node(6, 7, 5)
    }

    # Define the connections between nodes
    self.edges = {
      1: [3, 4],
      2: [1, 3],
      3: [1, 2, 5, 6],
      4: [1, 3, 5],
      5: [3, 4],
      6: [3]
    }

    self.cost = {
      (1, 3): 5,
      (1, 4): 6,
      (2, 1): 4,
      (2, 3): 4,
      (3, 1): 5,
      (3, 2): 5,
      (3, 5): 6,
      (3, 6): 7,
      (4, 1): 6,
      (4, 3): 5,
      (4, 5): 7,
      (5, 3): 6,
      (5, 4): 8,
      (6, 3): 7,
    }

 

# ---------- HEURISTIC ---------- #

# Define the heuristic function, the distance to closest goal
def heuristic(node_id, goal_ids, graph):
  node = graph.nodes[node_id]
  min_distance = float('inf')

  for goal_id in goal_ids:
    goal = graph.nodes[goal_id] 

    # Euclidean distance
    dx = node.x - goal.x
    dy = node.y - goal.y
    e_distance = math.sqrt((dx ** 2) + (dy ** 2))

    if e_distance < min_distance:
      min_distance = e_distance

  return min_distance



# ---------- EDGE COST ---------- #

# Check the edge cost
def edge_cost(from_id, to_id, graph):
  if (from_id, to_id) in graph.cost: 
    return graph.cost[(from_id, to_id)]
  return float('inf')



# ---------- IDA* ALGORITHM ---------- #


# Number of nodes created and the total cost (if needed later)
node_count = 0
total_cost = 0

# Define the search algorithm
def search(path, g, threshold, goal_ids, graph):
  # Count node created
  global node_count
  node_count += 1

  # Set the current id is the last node found
  current_id = path[-1]

  # Calculate the f(n), given that f(n) = g(n) + h(n)
  f = g + heuristic(current_id, goal_ids, graph)

  # If the f(n) larger than threshold, stop immediately
  if f > threshold:
    return f
  
  # If the current node is the goal -> solution found
  if current_id in goal_ids:
    global total_cost
    total_cost = g
    return "found"
  
  min_threshold = float('inf')

  # Checking the neighbor nodes from graph
  neighbors = graph.edges[current_id]

  for neighbor_id in neighbors:
    # Avoid cycle loop
    if neighbor_id not in path:
      # Calculate the cost from current node to neighbor
      cost = edge_cost(current_id, neighbor_id, graph)

      # Add the neighbor node to become the current node
      path.append(neighbor_id)

      # Repeat the process until find the solution
      result = search(path, g + cost, threshold, goal_ids, graph)

      if result == "found":
        return "found"
      
      if result < min_threshold:
        min_threshold = result

      # Backtrack
      path.pop()
  
  return min_threshold


# Define final search
def IDA_Star():
  # Initialization
  start_id=2
  goal_ids=[5, 4]
  graph=Graph()

  # Find the threshold by calculating the h(start)
  threshold = heuristic(start_id, goal_ids, graph)
  path = [start_id]

  # Increase the threshold gradually until reach the goal
  while True:
    result = search(path, 0, threshold, goal_ids, graph)

    if result == "found":
      return path
    
    if result == float('inf'):
      return "no solution"

    threshold = result



# ---------- EXECUTION ---------- #

path = IDA_Star()
print(f"{path[-1]} {node_count}")
print(f"{path}")
print(f"Total cost: {total_cost}")
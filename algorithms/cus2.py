# IDA* - Iterative Deepening A
import math

# Number of nodes created and the total cost (if needed later)
node_count = 0
total_cost = 0
 

# ---------- HEURISTIC ---------- #

# Define the heuristic function, the distance to closest goal
def heuristic(node_id, goal_ids, graph):
  node = graph.nodes[node_id]
  best = float("inf")

  for goal_id in goal_ids:
    goal = graph.nodes[goal_id]
    
    # Euclidean distance
    dx = node.x - goal.x
    dy = node.y - goal.y
    dist = math.sqrt(dx * dx + dy * dy)
    best = min(best, dist)

  return best



# ---------- EDGE COST ---------- #

# Check the edge cost
def edge_cost(a, b, graph):
  return graph.cost.get((a, b), float("inf"))



# ---------- IDA* ALGORITHM ---------- #

# Define the search algorithm
def search(path, g, threshold, goal_ids, graph):
  # Count node created
  global node_count, total_cost
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
      
      min_threshold = min(min_threshold, result)
      path.pop()
  
  return min_threshold


# Define final search
def IDA_Star(graph, start_id, goal_ids):
  # Initialization
  global node_count, total_cost
  node_count = 0
  total_cost = 0

  # Find the threshold by calculating the h(start)
  threshold = heuristic(start_id, goal_ids, graph)
  path = [start_id]

  # Increase the threshold gradually until reach the goal
  while True:
    result = search(path, 0, threshold, goal_ids, graph)

    if result == "found":
      return path, node_count, total_cost
    
    if result == float('inf'):
      return None, node_count, total_cost

    threshold = result
<<<<<<< HEAD
=======

>>>>>>> 879cedddbe4853c7966c8501708ff1235209ab2c

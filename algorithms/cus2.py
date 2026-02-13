# IDA* - Iterative Deepening A
import math

# Number of nodes created and the total cost (if needed later)
node_count = 0
total_cost = 0
 

# ---------- HEURISTIC ---------- #

# Define the heuristic function, the distance to closest goal
def heuristic(node_id, goal_ids, graph):
  # Thêm try-except và getattr để an toàn với cấu trúc graph mới
  try:
    if not hasattr(graph, 'nodes') or node_id not in graph.nodes:
      return 0
    node = graph.nodes[node_id]
    best = float("inf")

    for goal_id in goal_ids:
      if goal_id in graph.nodes:
        goal = graph.nodes[goal_id]
        
        # Euclidean distance
        dx = getattr(node, 'x', 0) - getattr(goal, 'x', 0)
        dy = getattr(node, 'y', 0) - getattr(goal, 'y', 0)
        dist = math.sqrt(dx * dx + dy * dy)
        best = min(best, dist)

    return best if best != float("inf") else 0
  except Exception:
    return 0


# ---------- EDGE COST ---------- #

# Check the edge cost (Hàm này giữ lại làm fallback cho an toàn)
def edge_cost(a, b, graph):
  if hasattr(graph, 'cost') and graph.cost is not None:
    return graph.cost.get((a, b), float("inf"))
  return 0 # Nếu graph không có dictionary cost thì trả về 0


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

  # Checking the neighbor nodes from graph (Tương thích với cấu trúc graph mới)
  if hasattr(graph, 'get_neighbors'):
    neighbors_raw = graph.get_neighbors(current_id)
  elif hasattr(graph, 'neighbors'):
    neighbors_raw = graph.neighbors(current_id)
  else:
    try:
        neighbors_raw = graph.edges[current_id]
    except:
        neighbors_raw = []

  # Sắp xếp neighbors để kết quả duyệt đồng nhất với các thuật toán khác
  if neighbors_raw and isinstance(neighbors_raw[0], tuple):
    neighbors_raw.sort(key=lambda x: int(x[0]))
  else:
    neighbors_raw.sort(key=lambda x: int(x))

  for item in neighbors_raw:
    # Tách id và cost một cách an toàn do cấu trúc mới trả về tuple
    if isinstance(item, tuple):
      neighbor_id = item[0]
      step_cost = item[1]
    else:
      neighbor_id = item
      step_cost = edge_cost(current_id, neighbor_id, graph)

    # Avoid cycle loop
    if neighbor_id not in path:
      # Calculate the cost from current node to neighbor (đã được tính ở step_cost)
      
      # Add the neighbor node to become the current node
      path.append(neighbor_id)

      # Repeat the process until find the solution
      result = search(path, g + step_cost, threshold, goal_ids, graph)

      if result == "found":
        return "found"
      
      min_threshold = min(min_threshold, result)
      
      # Backtrack
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
      return [], node_count, total_cost

    threshold = result
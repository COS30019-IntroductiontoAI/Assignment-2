# IDA* - Iterative Deepening A
import math

# Number of nodes created and the total cost (if needed later)
node_count = 0
total_cost = 0


# Define the heuristic function
# Since we are solving least moves,
# heuristic must estimate remaining number of moves.
# To guarantee optimality, we return 0.
def heuristic(node_id, goal_ids, graph):
    return 0 


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
        total_cost = g  # Number of moves
        return "found"

    min_threshold = float("inf")

    # Checking the neighbor nodes from graph
    if hasattr(graph, "get_neighbors"):
        neighbors_raw = graph.get_neighbors(current_id)
    elif hasattr(graph, "neighbors"):
        neighbors_raw = graph.neighbors(current_id)
    else:
        try:
            neighbors_raw = graph.edges[current_id]
        except:
            neighbors_raw = []

    # Arrange neighbors
    if neighbors_raw and isinstance(neighbors_raw[0], tuple):
        neighbors_raw.sort(key=lambda x: int(x[0]))
    else:
        neighbors_raw.sort(key=lambda x: int(x))

    for item in neighbors_raw:
        if isinstance(item, tuple):
            neighbor_id = item[0] 
        else:
            neighbor_id = item 

        # Avoid cycle loop
        if neighbor_id not in path:

            # Add the neighbor node to become the current node
            path.append(neighbor_id)

            # Repeat the process until find the solution
            # Each move counts as 1 (least moves objective)
            result = search(path, g + 1, threshold, goal_ids, graph)

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

    # Since heuristic = 0, start threshold = 0
    threshold = heuristic(start_id, goal_ids, graph)
    path = [start_id]

    # Increase the threshold gradually until reach the goal
    while True:
        result = search(path, 0, threshold, goal_ids, graph)

        if result == "found":
            return path, node_count, total_cost

        if result == float("inf"):
            return [], node_count, total_cost

        threshold = result
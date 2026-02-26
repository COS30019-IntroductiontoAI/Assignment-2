# IDA* - Iterative Deepening A*
import math
from utils import get_max_edge_length
from graph import Graph

# Number of nodes created and the total cost (if needed later)
node_count = 0
total_cost = 0


# Define the heuristic function
# Since we are solving least moves,
# heuristic must estimate remaining number of moves.
def heuristic(node_id, goal_ids, graph: Graph, max_edge: float):
    node_coords = graph.get_coordinates(node_id)
    if not node_coords:
        return 0

    min_h = float('inf')
    for goal_id in goal_ids:
        goal_coords = graph.get_coordinates(goal_id)
        if goal_coords:
            dist = math.sqrt((node_coords[0] - goal_coords[0])**2 +
                             (node_coords[1] - goal_coords[1])**2)
            min_h = min(min_h, dist / max_edge)

    return math.ceil(min_h) if min_h != float('inf') else 0


# Define the search algorithm
def search(path, g, threshold, goal_ids, graph, max_edge):
    # Count nodes created
    global node_count, total_cost
    node_count += 1

    # Current node is the last node in the path
    current_id = path[-1]

    # Calculate f(n) = g(n) + h(n)
    f = g + heuristic(current_id, goal_ids, graph, max_edge)

    # If f(n) exceeds threshold, prune and return f as next threshold candidate
    if f > threshold:
        return f

    # If current node is a goal -> solution found
    if current_id in goal_ids:
        total_cost = g  # Number of moves to reach goal
        return "found"

    min_threshold = float("inf")

    # Get neighbors from graph
    if hasattr(graph, "get_neighbors"):
        neighbors_raw = graph.get_neighbors(current_id)
    elif hasattr(graph, "neighbors"):
        neighbors_raw = graph.neighbors(current_id)
    else:
        try:
            neighbors_raw = graph.edges[current_id]
        except:
            neighbors_raw = []

    # Sort neighbors for deterministic expansion order
    if neighbors_raw and isinstance(neighbors_raw[0], tuple):
        neighbors_raw.sort(key=lambda x: int(x[0]))
    else:
        neighbors_raw.sort(key=lambda x: int(x))

    for item in neighbors_raw:
        if isinstance(item, tuple):
            neighbor_id = item[0]
        else:
            neighbor_id = item

        # Avoid cycles
        if neighbor_id not in path:

            # Expand neighbor
            path.append(neighbor_id)

            # Each move costs 1 (least-moves objective)
            result = search(path, g + 1, threshold, goal_ids, graph, max_edge)

            if result == "found":
                return "found"

            min_threshold = min(min_threshold, result)

            # Backtrack
            path.pop()

    return min_threshold


# Define final search entry point
def IDA_Star(graph, start_id, goal_ids):
    global node_count, total_cost
    node_count = 0
    total_cost = 0

    # Precompute max edge length once, used by heuristic on every node expansion
    max_edge = get_max_edge_length(graph)

    # Initial threshold is the heuristic estimate from the start node
    threshold = heuristic(start_id, goal_ids, graph, max_edge)
    path = [start_id]

    # Increase threshold gradually until goal is found
    while True:
        result = search(path, 0, threshold, goal_ids, graph, max_edge)

        if result == "found":
            return path, node_count, total_cost

        if result == float("inf"):
            return [], node_count, total_cost

        threshold = result
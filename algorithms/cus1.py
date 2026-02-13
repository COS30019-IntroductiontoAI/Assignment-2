# CUS1 - Iterative Deepening Search (IDS)

def cus1(graph, start, goal_ids):
    depth = 0
    # Use a dictionary to track explored nodes across recursive calls
    stats = {'nodes_explored': 0} 
    
    # Maximum depth limit to prevent infinite loops if no path exists
    max_depth = 1000 

    while depth < max_depth:
        # Call Depth-Limited Search (DLS)
        # Initialize path as [start] and cost as 0
        path, total_cost = depth_limited_search(graph, start, goal_ids, depth, [start], 0, stats)

        if path is not None:
            return path, stats['nodes_explored'], total_cost

        depth += 1
        
    # No path found
    return [], stats['nodes_explored'], 0


# Depth-Limited Search
def depth_limited_search(graph, current, goal_ids, depth, current_path, current_cost, stats):
    # Increment explored count each time the function is called
    stats['nodes_explored'] += 1

    # Goal test: check if the current node is a destination
    if current in goal_ids:
        return current_path, current_cost

    # Reached the depth limit for the current iteration
    if depth == 0:
        return None, 0

    # Get neighbors (Support both method names for compatibility)
    if hasattr(graph, 'get_neighbors'):
        neighbors_raw = graph.get_neighbors(current)
    elif hasattr(graph, 'neighbors'):
        neighbors_raw = graph.neighbors(current)
    else:
        neighbors_raw = []

    # Safely sort neighbors (Ascending order) handling tuples
    if neighbors_raw and isinstance(neighbors_raw[0], tuple):
        neighbors_raw.sort(key=lambda x: int(x[0]))
    else:
        neighbors_raw.sort(key=lambda x: int(x))

    for item in neighbors_raw:
        # Safely extract node id and step cost
        if isinstance(item, tuple):
            neighbor = item[0]
            step_cost = item[1]
        else:
            neighbor = item
            step_cost = 0

        # Cycle avoidance: only visit nodes not currently in the path
        if neighbor not in current_path:
            # Recursively search deeper
            result_path, result_cost = depth_limited_search(
                graph, 
                neighbor, 
                goal_ids, 
                depth - 1, 
                current_path + [neighbor], 
                current_cost + step_cost, 
                stats
            )

            # If a path to the goal is found in this branch, return it immediately
            if result_path is not None:
                return result_path, result_cost

    return None, 0
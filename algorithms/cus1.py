# CUS1 - Iterative Deepening Search (IDS)

def cus1(graph, start, goal_ids):
    depth = 0
    
    # Count nodes generated (start node counts as 1)
    stats = {'nodes_generated': 1}

    max_depth = 1000

    while depth < max_depth:
        path, total_cost = depth_limited_search(
            graph,
            start,
            goal_ids,
            depth,
            [start],
            0,
            stats
        )

        if path is not None:
            return path, stats['nodes_generated'], total_cost

        depth += 1

    return [], stats['nodes_generated'], 0


def depth_limited_search(graph, current, goal_ids, depth, current_path, current_cost, stats):

    # Goal test
    if current in goal_ids:
        return current_path, current_cost

    if depth == 0:
        return None, 0

    # Get neighbors
    if hasattr(graph, 'get_neighbors'):
        neighbors_raw = graph.get_neighbors(current)
    elif hasattr(graph, 'neighbors'):
        neighbors_raw = graph.neighbors(current)
    else:
        neighbors_raw = []

    # Sort ascending
    if neighbors_raw and isinstance(neighbors_raw[0], tuple):
        neighbors_raw.sort(key=lambda x: int(x[0]))
    else:
        neighbors_raw.sort(key=lambda x: int(x))

    for item in neighbors_raw:

        if isinstance(item, tuple):
            neighbor = item[0]
            step_cost = item[1]
        else:
            neighbor = item
            step_cost = 0

        # Avoid cycle
        if neighbor not in current_path:

            # ✅ COUNT NODE GENERATED HERE
            stats['nodes_generated'] += 1

            result_path, result_cost = depth_limited_search(
                graph,
                neighbor,
                goal_ids,
                depth - 1,
                current_path + [neighbor],
                current_cost + step_cost,
                stats
            )

            if result_path is not None:
                return result_path, result_cost

    return None, 0
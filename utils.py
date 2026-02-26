import math
from graph import Graph


def euclidean_distance(node1, node2):
    # Euclidean distance between two graph nodes.
    # Used only as an estimate (heuristic), not real path cost.
    return math.sqrt(
        (node1.x - node2.x) ** 2 +
        (node1.y - node2.y) ** 2
    )


def heuristic(node, graph, destinations):
    # Heuristic function h(n).
    # Because there may be multiple destination nodes,
    # estimate distance to the closest destination.
    if not destinations:
        return math.inf

    return min(
        euclidean_distance(node, graph.nodes[goal])
        for goal in destinations
    )


def get_max_edge_length(graph: Graph):
    # Use for least moves strategy of CUS2 - IDA*
    # If the longest any single edge can "cover" in distance is X
    # Then the fewest moves needed to cover remaining distance is distance / X
    max_len = 0
    for from_id in graph.edges:
        for (to_id, cost) in graph.edges[from_id]:
            x1, y1 = graph.get_coordinates(from_id)
            x2, y2 = graph.get_coordinates(to_id)
            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            max_len = max(max_len, dist)
    return max_len


def reconstruct_path(search_node):
    # Reconstruct path by following parent links
    # from goal node back to the origin.
    path = []
    current = search_node

    while current is not None:
        path.append(current.state)
        current = current.parent

    path.reverse()
    return path


def reconstruct_path_from_came_from(came_from, current):
    # Rebuild path from goal node back to start node
    # using a parent map (used by BFS/DFS).
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

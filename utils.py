import math


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

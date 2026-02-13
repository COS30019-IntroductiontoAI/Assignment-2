import math


def euclidean_distance(node1, node2):
    """
    Euclidean distance between two graph nodes.
    Used ONLY as an estimate (heuristic), not real path cost.
    """
    return math.sqrt(
        (node1.x - node2.x) ** 2 +
        (node1.y - node2.y) ** 2
    )


def heuristic(node, graph, destinations):
    """
    Heuristic function h(n).

    Because there may be multiple destination nodes,
    we estimate the distance to the CLOSEST destination.
    """
    if not destinations:
        return math.inf

    return min(
        euclidean_distance(node, graph.nodes[goal])
        for goal in destinations
    )


def reconstruct_path(search_node):
    """
    Reconstruct the path by following parent links
    from the goal node back to the origin.
    """
    path = []
    current = search_node

    while current is not None:
        path.append(current.state)
        current = current.parent

    path.reverse()
    return path
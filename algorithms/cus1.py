import math


# Calculate straight-line distance between two nodes
def euclidean(node_a, node_b):
    dx = node_a.x - node_b.x
    dy = node_a.y - node_b.y
    return math.sqrt(dx * dx + dy * dy)


# Calculate grid-based distance between two nodes
def manhattan(node_a, node_b):
    return abs(node_a.x - node_b.x) + abs(node_a.y - node_b.y)


# Select and return the heuristic function based on input name
def get_heuristic(name):
    name = name.lower()

    if name == "euclidean":
        return euclidean
    elif name == "manhattan":
        return manhattan
    else:
        raise ValueError(
            f"Unknown heuristic '{name}'. "
            "Supported heuristics: euclidean, manhattan"
        )

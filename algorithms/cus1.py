# CUS1 - Iterative Deepening Search (IDS)

def cus1(graph, start, goal):
    depth = 0

    while True:
        visited = set()
        path = depth_limited_search(graph, start, goal, depth, visited)

        if path:
            return path

        depth += 1


# Depth-Limited DFS
def depth_limited_search(graph, current, goal, depth, visited):
    if depth < 0:
        return None

    visited.add(current)

    if current == goal:
        return [current]

    if depth == 0:
        return None

    # Sort neighbors to ensure consistent traversal order
    neighbors = sorted(graph.get_neighbors(current), key=lambda x: x[0])

    for neighbor, _ in neighbors:
        if neighbor not in visited:
            result = depth_limited_search(
                graph, neighbor, goal, depth - 1, visited
            )

            if result:
                return [current] + result

    return None
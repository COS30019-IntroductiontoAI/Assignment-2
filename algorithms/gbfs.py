import heapq
from algorithms.cus1 import get_heuristic


# Greedy Best-First Search using a heuristic function
def gbfs(graph, start, goal, heuristic_type="euclidean"):
    # Select the heuristic function based on input
    heuristic = get_heuristic(heuristic_type)

    # Priority queue storing nodes ordered by heuristic value
    frontier = []
    heapq.heappush(frontier, (0, start))

    # Track visited nodes and parent relationships
    came_from = {}
    visited = set()

    # Main GBFS loop
    while frontier:
        _, current = heapq.heappop(frontier)

        if current in visited:
            continue
        visited.add(current)

        # Stop search when the goal is reached
        if current == goal:
            return reconstruct_path(came_from, start, goal)

        # Expand neighbors of the current node
        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in visited:
                priority = heuristic(
                    graph.nodes[neighbor],
                    graph.nodes[goal]
                )
                heapq.heappush(frontier, (priority, neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current

    # Return None if no path is found
    return None


# Reconstruct the path from start to goal using parent links
def reconstruct_path(came_from, start, goal):
    path = [goal]

    # Trace back from goal to start
    while path[-1] != start:
        path.append(came_from[path[-1]])

    path.reverse()
    return path
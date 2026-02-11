import heapq
import math


# Euclidean distance
def euclidean(node_a, node_b):
    dx = node_a.x - node_b.x
    dy = node_a.y - node_b.y
    return math.sqrt(dx * dx + dy * dy)


# Greedy Best First Search
def gbfs(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))

    visited = set()
    came_from = {}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in visited:
                priority = euclidean(
                    graph.nodes[neighbor],
                    graph.nodes[goal]
                )
                heapq.heappush(frontier, (priority, neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current

    return None


# Build path
def reconstruct_path(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

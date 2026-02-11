from collections import deque


# CUS1 - Uninformed Search (Breadth First Search)
def cus1(graph, start, goal):
    frontier = deque([start])      # FIFO queue
    visited = set([start])         # Track visited nodes
    came_from = {}                 # Track path

    while frontier:
        current = frontier.popleft()

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for neighbor, _ in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                frontier.append(neighbor)

    return None


# Build final path
def reconstruct_path(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

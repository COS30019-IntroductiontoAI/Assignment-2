from collections import deque

def bfs(graph, start_node, goal_nodes):
    # Initialize queue with start node
    queue = deque([start_node])
    
    # Track visited nodes to avoid revisiting
    visited = set([start_node])
    
    # Store parent of each node for path reconstruction
    came_from = {start_node: None}
    
    # Count how many nodes are explored
    explored_count = 0

    while queue:
        # Remove node from front of queue (FIFO)
        current_node = queue.popleft()
        explored_count += 1
        
        # Check if current node is a goal
        if current_node in goal_nodes:
            path = reconstruct_path(came_from, current_node)
            return current_node, explored_count, path
        
        # Get neighbors of the current node from the graph
        neighbors = graph.get_neighbors(current_node)
        
        # Sort neighbors in ascending order by numeric ID
        neighbors.sort(key=lambda x: int(x))
        
        for next_node in neighbors:
            # Visit node if not visited before
            if next_node not in visited:
                visited.add(next_node)
                came_from[next_node] = current_node  # Store parent node
                queue.append(next_node)

    # Return if no path is found
    return None, explored_count, []

def reconstruct_path(came_from, current):
    """Rebuild path from goal to start"""
    path = []
    
    # Trace back using parent links
    while current is not None:
        path.append(current)
        current = came_from[current]
        
    # Reverse to get path from start to goal
    path.reverse()
    return path

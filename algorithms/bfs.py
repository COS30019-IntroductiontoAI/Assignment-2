from collections import deque

def bfs(graph, start_node, goal_nodes):
    # Initialize queue with start node
    queue = deque([start_node])
    
    # Track visited nodes to avoid revisiting
    visited = set([start_node])
    
    # Store parent of each node for path reconstruction
    came_from = {start_node: None}
    
    # Track total cost to reach each node
    cost_so_far = {start_node: 0}
    
    # Count how many nodes are explored
    explored_count = 0

    while queue:
        # Remove node from front of queue (FIFO)
        current_node = queue.popleft()
        explored_count += 1
        
        # Check if current node is a goal
        if current_node in goal_nodes:
            path = reconstruct_path(came_from, current_node)
            total_cost = cost_so_far[current_node]
            return path, explored_count, total_cost
        
        # Get neighbors of the current node from the graph
        neighbors = graph.get_neighbors(current_node)
        
        if neighbors and isinstance(neighbors[0], tuple):
            neighbors.sort(key=lambda x: int(x[0]))
        else:
            neighbors.sort(key=lambda x: int(x))
        
        for neighbor in neighbors:
            if isinstance(neighbor, tuple):
                next_node = neighbor[0]
                step_cost = neighbor[1]
            else:
                next_node = neighbor
                step_cost = 0

            # Visit node if not visited before
            if next_node not in visited:
                visited.add(next_node)
                came_from[next_node] = current_node
                cost_so_far[next_node] = cost_so_far[current_node] + step_cost
                queue.append(next_node)

    # Return if no path is found
    return [], explored_count, 0

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
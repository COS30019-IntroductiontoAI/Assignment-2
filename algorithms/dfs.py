def dfs(graph, start_node, goal_nodes):
    """
    Perform Depth-First Search (DFS).
    Uses a stack (list) to manage nodes.
    """
    # Initialize stack with start node
    stack = [start_node]
    
    # Track visited nodes to avoid cycles
    visited = set()
    
    # Store parent of each node for path reconstruction
    came_from = {start_node: None}
    
    # Track total cost to reach each node
    cost_so_far = {start_node: 0}
    
    # Count explored nodes
    explored_count = 0

    while stack:
        # Pop node from top of stack (LIFO)
        current_node = stack.pop()
        
        # Skip if node already processed
        if current_node in visited:
            continue
            
        # Mark node as visited
        visited.add(current_node)
        explored_count += 1
        
        # Check if current node is a goal
        if current_node in goal_nodes:
            path = reconstruct_path(came_from, current_node)
            total_cost = cost_so_far[current_node]
            return path, explored_count, total_cost

        # Get neighbors of current node
        neighbors = graph.get_neighbors(current_node)
        
        if neighbors and isinstance(neighbors[0], tuple):
            neighbors.sort(key=lambda x: int(x[0]), reverse=True)
        else:
            neighbors.sort(key=lambda x: int(x), reverse=True)
        
        for neighbor in neighbors:
            # Tách id và cost một cách an toàn
            if isinstance(neighbor, tuple):
                next_node = neighbor[0]
                step_cost = neighbor[1]
            else:
                next_node = neighbor
                step_cost = 0
                
            if next_node not in visited:
                # Record parent and cost only if not recorded before
                if next_node not in came_from:
                    came_from[next_node] = current_node
                    cost_so_far[next_node] = cost_so_far[current_node] + step_cost
                stack.append(next_node)

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
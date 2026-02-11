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
            return current_node, explored_count, path

        # Get neighbors of current node
        neighbors = graph.get_neighbors(current_node)
        
        # Sort neighbors in descending order
        # This ensures smaller node IDs are explored first
        # when using LIFO stack behavior
        neighbors.sort(key=lambda x: int(x), reverse=True)
        
        for next_node in neighbors:
            if next_node not in visited:
                # Record parent only if not recorded before
                if next_node not in came_from:
                    came_from[next_node] = current_node
                stack.append(next_node)

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

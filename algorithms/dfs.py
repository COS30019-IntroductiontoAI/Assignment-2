from utils import reconstruct_path_from_came_from


def dfs(graph, start_node, goal_nodes):
    # Initialize stack with start node
    stack = [start_node]
    
    # Track visited nodes to avoid cycles
    visited = set()
    
    # Store parent of each node for path reconstruction
    came_from = {start_node: None}
    # Track total cost to reach each node
    cost_so_far = {start_node: 0}
    
    created_count = 1

    while stack:
        # Pop node from top of stack (LIFO)
        current_node = stack.pop()
        
        # Skip if node already processed
        if current_node in visited:
            continue
            
        # Mark node as visited
        visited.add(current_node)
        
        # Check if current node is a goal
        if current_node in goal_nodes:
            path = reconstruct_path_from_came_from(came_from, current_node)
            total_cost = cost_so_far[current_node]
            return path, created_count, total_cost

        # Get neighbors of current node
        neighbors = graph.get_neighbors(current_node)
        
        if neighbors and isinstance(neighbors[0], tuple):
            neighbors.sort(key=lambda x: int(x[0]), reverse=True)
        else:
            neighbors.sort(key=lambda x: int(x), reverse=True)
        
        for neighbor in neighbors:
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
                
                created_count += 1

    # Return if no path is found
    return [], created_count, 0

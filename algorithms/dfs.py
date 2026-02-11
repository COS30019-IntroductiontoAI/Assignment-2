# --- DATA STRUCTURES ---
class Node:
    def __init__(self, id, x, y):
        self.id = id; self.x = x; self.y = y

class Graph:
    def __init__(self):
        self.nodes = {
            1: Node(1, 4, 1), 
            2: Node(2, 2, 2), 
            3: Node(3, 4, 4),
            4: Node(4, 6, 3), 
            5: Node(5, 5, 6), 
            6: Node(6, 7, 5)
        }
        
        #Adjacency list(Directed Edges)
        self.edges = {
            1: [3, 4], 
            2: [1, 3], 
            3: [1, 2, 5, 6],
            4: [1, 3, 5], 
            5: [3, 4], 
            6: [3]
        }
        
        self.cost = {
            (2,1): 4, 
            (3,1): 5, 
            (1,3): 5, 
            (2,3): 4, 
            (3,2): 5,
            (4,1): 6, 
            (1,4): 6, 
            (4,3): 5, 
            (3,5): 6, 
            (5,3): 6,
            (4,5): 7, 
            (5,4): 8, 
            (6,3): 7, 
            (3,6): 7
        }

#FUNCTIONS
def calculate_total_cost(path, graph):
    #Sum up edge costs
    total = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        if (u, v) in graph.cost:
            total += graph.cost[(u, v)]
    return total

def reconstruct_path(came_from, current):
    #Backtrack from goal to start
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

# MAIN ALGORITHM 
def run_dfs():
    # Configuration
    start_node = 2
    goal_nodes = [5, 4]
    graph = Graph()
    
    # Initialize Stack
    stack = [start_node]
    visited = set()
    came_from = {start_node: None} # Track parent
    node_count = 0
    
    while stack:
        # Pop from the end (LIFO behavior)
        current = stack.pop()
        
        # Skip if visited in another branch
        if current in visited:
            continue
            
        visited.add(current)
        node_count += 1
        
        # Check if goal reached
        if current in goal_nodes:
            path = reconstruct_path(came_from, current)
            cost = calculate_total_cost(path, graph)
            
            # Output formatted result
            path_str = " ".join(str(x) for x in path)
            print("PathFinder-test.txt DFS")
            print(f"{current} {node_count} {path_str}")
            print(f"Total cost: {cost}")
            return

        # Expand neighbors
        if current in graph.edges:
            neighbors = graph.edges[current]
            
            # SORT DESCENDING 
            neighbors.sort(reverse=True) 
            
            for next_node in neighbors:
                if next_node not in visited:
                    # Update parent if not already set
                    if next_node not in came_from:
                        came_from[next_node] = current
                    stack.append(next_node)

    print("No path found")

if __name__ == "__main__":
    run_dfs()
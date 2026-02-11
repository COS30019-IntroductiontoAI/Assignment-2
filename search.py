import sys
from graph import Graph
import parser

# Import search algorithms
from algorithms.bfs import bfs
from algorithms.dfs import dfs

def main():
    # Expected format:
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        return

    filename = sys.argv[1]
    
    # Convert method to uppercase for easier comparison
    method = sys.argv[2].upper()

    # 2. Initialize graph and read input file
    graph = Graph()
    origin, destinations = parser.read_file(filename, graph)

    # Stop if file reading fails
    if origin is None:
        return

    #Select search algorithm based on method
    result = None
    
    if method == "BFS":
        result = bfs(graph, origin, destinations)
        
    elif method == "DFS":
        result = dfs(graph, origin, destinations)
        
    else:
        print(f"Method {method} not supported.")
        return

    # filename method
    # goal number_of_nodes path
    goal_node, num_nodes, path = result

    print(f"{filename} {method}")
    
    if goal_node:
        # Convert path list into space-separated string
        path_str = " ".join(path)
        print(f"{goal_node} {num_nodes} {path_str}")
    else:
        # Output when no path is found
        print(f"No path found. Nodes visited: {num_nodes}")

if __name__ == "__main__":
    main()

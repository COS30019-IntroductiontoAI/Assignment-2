import sys
from parser import parse_file
from algorithms.gbfs import gbfs


# Entry point for running the search program
def main():
    # Validate command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python search.py <filename> GBFS [euclidean|manhattan]")
        return

    # Read input parameters from command line
    filename = sys.argv[1]
    algorithm = sys.argv[2]
    heuristic = sys.argv[3] if len(sys.argv) > 3 else "euclidean"

    # Parse input file to build the graph and search parameters
    graph, origin, destinations = parse_file(filename)

    # Ensure only GBFS algorithm is executed
    if algorithm != "GBFS":
        print("Only GBFS is supported.")
        return

    # Run GBFS for each destination node
    for goal in destinations:
        try:
            path = gbfs(graph, origin, goal, heuristic)
            if path:
                print(f"{goal} {len(path)}")
                print(" -> ".join(map(str, path)))
            else:
                print(f"No path found to {goal}")
        except ValueError as e:
            print(e)
            return


# Execute main function when the script is run directly
if __name__ == "__main__":
    main()

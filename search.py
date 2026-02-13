import sys
from parser import parse_file
from algorithms.gbfs import GBFS

def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        return

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    graph, origin, destinations = parse_file(filename)

    if method != "GBFS":
        print("Only GBFS is supported in this version.")
        return

    solver = GBFS(graph, origin, destinations)
    goal, nodes_created, path = solver.search()

    print(f"{filename} {method}")
    print(f"{goal} {nodes_created}")
    print(" -> ".join(map(str, path)))

if __name__ == "__main__":
    main()

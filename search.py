import sys
from parser import parse_file
from algorithms.gbfs import gbfs
from algorithms.cus1 import cus1


# Entry point
def main():
    if len(sys.argv) < 3:
        print("Usage: python search.py <filename> [GBFS|CUS1]")
        return

    filename = sys.argv[1]
    algorithm = sys.argv[2]

    graph, origin, destinations = parse_file(filename)

    for goal in destinations:
        if algorithm == "GBFS":
            path = gbfs(graph, origin, goal)

        elif algorithm == "CUS1":
            path = cus1(graph, origin, goal)

        else:
            print("Unsupported algorithm.")
            return

        if path:
            print(f"{goal} {len(path)}")
            print(" -> ".join(map(str, path)))
        else:
            print(f"No path found to {goal}")


if __name__ == "__main__":
    main()

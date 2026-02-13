import sys
from parser import parse_problem
from astar import astar_search


def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        return

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    try:
        graph, origin, destinations = parse_problem(filename)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}")
        return

    if method == "AS":
        method = "A*"
        goal, node_count, path = astar_search(graph, origin, destinations)

        # Output format strictly follows assignment specification
        print(filename, method)
        print(goal, node_count)
        print(" ".join(map(str, path)))
    else:
        print("Search method not implemented.")


if __name__ == "__main__":
    main()

from graph import Graph


# Parse problem from txt file
def parse_problem_file(filename):
    graph = Graph()
    start_id = None
    goal_ids = []

    section = None

    # Open the file from command line
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()

            # If blank, continue
            if not line:
                continue

            # Mark each section with their name
            if line.startswith("Nodes:"):
                section = "nodes"
                continue
            elif line.startswith("Edges:"):
                section = "edges"
                continue
            elif line.startswith("Origin:"):
                section = "origin"
                continue
            elif line.startswith("Destinations:"):
                section = "dest"
                continue

            # Extract the node number and coordinate
            if section == "nodes":
                # 1: (4,1)
                left, right = line.split(":")
                node_id = int(left.strip())

                coords = right.strip().replace("(", "").replace(")", "")
                x, y = coords.split(",")
                graph.add_node(node_id, int(x), int(y))

            # Extract the edges path and its cost
            elif section == "edges":
                # (2,1): 4
                left, right = line.split(":")
                node_ids = left.strip().replace("(", "").replace(")", "")
                a, b = node_ids.split(",")

                cost = int(right.strip())
                graph.add_edge(int(a), int(b), cost)

            # Extract the origin node
            elif section == "origin":
                start_id = int(line)

            # Extract the destination nodes
            elif section == "dest":
                goal_ids = [int(x.strip()) for x in line.split(";")]

    return graph, start_id, goal_ids

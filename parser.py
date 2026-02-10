from graph import Graph

# Parse the input file and construct the graph data structure
def parse_file(filename):
    graph = Graph()
    origin = None
    destinations = []

    # Read all non-empty lines from the input file
    with open(filename, "r") as file:
        lines = [line.strip() for line in file if line.strip()]

    section = None

    # Process each section of the input file
    for line in lines:
        if line.endswith(":"):
            section = line
            continue

        # Parse node definitions
        if section == "Nodes:":
            node_id, coord = line.split(":")
            x, y = coord.strip()[1:-1].split(",")
            graph.add_node(int(node_id), int(x), int(y))

        # Parse edge definitions
        elif section == "Edges:":
            nodes, cost = line.split(":")
            from_node, to_node = nodes.strip()[1:-1].split(",")
            graph.add_edge(int(from_node), int(to_node), int(cost))

        # Parse origin node
        elif section == "Origin:":
            origin = int(line)

        # Parse destination nodes
        elif section == "Destinations:":
            destinations = [int(d) for d in line.split(";")]

    # Return the constructed graph and search parameters
    return graph, origin, destinations

from graph import Graph

def parse_file(filename):
    graph = Graph()
    origin = None
    destinations = []

    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]

        # Parse nodes
        if line == "Nodes:":
            i += 1
            while i < len(lines) and "(" in lines[i]:
                node_part, coord_part = lines[i].split(":")
                node_id = int(node_part.strip())
                x, y = coord_part.strip()[1:-1].split(",")
                graph.add_node(node_id, (int(x), int(y)))
                i += 1

        # Parse edges
        elif line == "Edges:":
            i += 1
            while i < len(lines) and lines[i].startswith("("):
                edge_part, cost_part = lines[i].split(":")
                src, dst = edge_part.strip()[1:-1].split(",")
                graph.add_edge(int(src), int(dst), int(cost_part.strip()))
                i += 1

        # Parse origin
        elif line == "Origin:":
            i += 1
            origin = int(lines[i])
            i += 1

        # Parse destinations
        elif line == "Destinations:":
            i += 1
            destinations = [int(x.strip()) for x in lines[i].split(";")]
            i += 1

        else:
            i += 1

    return graph, origin, destinations

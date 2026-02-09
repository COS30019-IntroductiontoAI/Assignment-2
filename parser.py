from graph import Graph, Node


def parse_problem(filename):
    """
    Parse the input problem file.

    Returns:
        graph (Graph)        : graph representation
        origin (int)         : origin node ID
        destinations (list) : list of destination node IDs
    """

    graph = Graph()
    origin = None
    destinations = []

    current_section = None   # Keeps track of which section we are reading

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            # Section headers end with ':'
            if line.endswith(":"):
                current_section = line[:-1]  # e.g., "Nodes", "Edges"
                continue

            if current_section == "Nodes":
                # Format: 1: (4,1)
                node_id, rest = line.split(":")
                x, y = rest.strip()[1:-1].split(",")  # remove '(' and ')'
                node_id = int(node_id)
                if node_id in graph.nodes:
                    raise ValueError(f"Duplicate node ID: {node_id}")
                graph.add_node(Node(node_id, int(x), int(y)))

            elif current_section == "Edges":
                # Format: (2,1): 4   -> edge 2 -> 1 with cost 4
                edge, cost = line.split(":")
                from_id, to_id = edge.strip()[1:-1].split(",")
                from_id = int(from_id)
                to_id = int(to_id)
                cost = int(cost)
                if cost < 0:
                    raise ValueError(f"Negative edge cost not allowed: {from_id}->{to_id} cost {cost}")
                graph.add_edge(from_id, to_id, cost)

            elif current_section == "Origin":
                # Only one origin node
                origin = int(line)

            elif current_section == "Destinations":
                # Possibly multiple destinations separated by ';'
                destinations = [int(x.strip()) for x in line.split(";") if x.strip()]

    if origin is None:
        raise ValueError("Origin section missing or empty.")
    if origin not in graph.nodes:
        raise ValueError(f"Origin node ID not found in Nodes: {origin}")
    if not destinations:
        raise ValueError("Destinations section missing or empty.")
    missing = [d for d in destinations if d not in graph.nodes]
    if missing:
        raise ValueError(f"Destination node IDs not found in Nodes: {missing}")
    if any(node_id not in graph.adjacency for node_id in graph.nodes):
        raise ValueError("Internal graph error: adjacency list missing for some nodes.")

    return graph, origin, destinations

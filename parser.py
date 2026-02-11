import re

def read_file(filename, graph):
    # Track which section of the file is currently being read
    current_section = None
    
    # Store start node and goal nodes
    origin = None
    destinations = []

    try:
        # Open and read all lines from file
        with open(filename, 'r') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue

            # Detect section keywords
            if line.startswith("Nodes:"):
                current_section = "NODES"
                continue
            elif line.startswith("Edges:"):
                current_section = "EDGES"
                continue
            elif line.startswith("Origin:"):
                current_section = "ORIGIN"
                continue
            elif line.startswith("Destinations:"):
                current_section = "DESTINATIONS"
                continue

            # Process data based on current section
            if current_section == "NODES":
                # Format: 1: (4,1)
                match = re.match(r"(\w+):\s*\((\d+),(\d+)\)", line)
                if match:
                    node_id, x, y = match.groups()
                    graph.add_node(node_id, (int(x), int(y)))

            elif current_section == "EDGES":
                # Format: (2,1): 4
                match = re.match(r"\((\w+),(\w+)\):\s*(\d+)", line)
                if match:
                    u, v, cost = match.groups()
                    graph.add_edge(u, v, float(cost))

            elif current_section == "ORIGIN":
                # Store starting node
                origin = line.strip()

            elif current_section == "DESTINATIONS":
                # Format: 5; 4
                dests = line.split(';')
                
                # Remove extra spaces from each destination
                destinations = [d.strip() for d in dests]

        return origin, destinations

    except FileNotFoundError:
        # Handle missing input file
        print(f"Error: File {filename} not found.")
        return None, []

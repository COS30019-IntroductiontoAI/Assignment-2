# parser.py
import re

def read_file(filename, graph):
    """
    Đọc file input và cập nhật thông tin vào đối tượng graph.
    Trả về: (origin, destinations)
    """
    current_section = None
    origin = None
    destinations = []

    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Xác định phần đang đọc (Keywords)
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

            # Xử lý dữ liệu từng phần
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
                # Format: 2
                origin = line.strip()

            elif current_section == "DESTINATIONS":
                # Format: 5; 4
                dests = line.split(';')
                destinations = [d.strip() for d in dests]

        return origin, destinations

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None, []
class Node:
    """
    Represents a node in the graph.

    NOTE:
    This is NOT a search node.
    It only stores information given in the problem (ID and coordinates).
    """

    def __init__(self, node_id, x, y):
        self.id = node_id      # Node ID (e.g., 1, 2, 3...)
        self.x = x             # x-coordinate (used for heuristic)
        self.y = y             # y-coordinate (used for heuristic)


class Graph:
    """
    Directed weighted graph using adjacency list representation.

    adjacency[node_id] = [(neighbor_id, cost), ...]
    """

    def __init__(self):
        self.nodes = {}        # node_id -> Node object
        self.adjacency = {}    # node_id -> list of outgoing edges

    def add_node(self, node):
        # Add a node and prepare its adjacency list
        self.nodes[node.id] = node
        self.adjacency[node.id] = []

    def add_edge(self, from_id, to_id, cost):
        # Add a directed edge (from_id -> to_id) with given cost
        if from_id not in self.adjacency:
            raise ValueError(f"Edge references unknown from-node ID: {from_id}")
        if to_id not in self.nodes:
            raise ValueError(f"Edge references unknown to-node ID: {to_id}")
        self.adjacency[from_id].append((to_id, cost))

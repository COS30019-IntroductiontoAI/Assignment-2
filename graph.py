class Node:
    """
    Represents a node in the graph.
    Stores only problem data (id and coordinates).
    """

    def __init__(self, node_id, x, y):
        self.id = node_id
        self.x = x
        self.y = y


class Graph:
    """
    Directed weighted graph using adjacency list.

    self.nodes[node_id] = Node object
    self.edges[node_id] = [(neighbor_id, cost), ...]
    """

    def __init__(self):
        self.nodes = {}
        self.edges = {}



    # -------------------------
    # Node & Edge Construction
    # -------------------------

    def add_node(self, node_id, x, y):
        self.nodes[node_id] = Node(node_id, x, y)
        if node_id not in self.edges:
            self.edges[node_id] = []

    def add_edge(self, from_node, to_node, cost):
        if from_node not in self.nodes:
            raise ValueError(f"Unknown from-node {from_node}")
        if to_node not in self.nodes:
            raise ValueError(f"Unknown to-node {to_node}")

        self.edges[from_node].append((to_node, cost))



    # -------------------------
    # Graph Query Functions
    # -------------------------

    def get_neighbors(self, node_id):
        # Returns list of (neighbor_id, cost)
        return self.edges.get(node_id, [])

    def get_cost(self, from_node, to_node):
        # Returns cost of edge from_node -> to_node
        for neighbor, cost in self.edges.get(from_node, []):
            if neighbor == to_node:
                return cost
        return float('inf')

    def get_coordinates(self, node_id):
        # Returns (x, y) coordinates of node
        node = self.nodes.get(node_id)
        if node:
            return (node.x, node.y)
        return None

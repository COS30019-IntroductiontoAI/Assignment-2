class Node:
    def __init__(self, node_id, x, y):
        # Initialize a node with an id and 2D coordinates
        self.id = node_id
        self.x = x
        self.y = y


class Graph:
    def __init__(self):
        # Initialize graph with node and edge containers
        self.nodes = {}
        self.edges = {}

    def add_node(self, node_id, x, y):
        # Add a node object into the graph
        self.nodes[node_id] = Node(node_id, x, y)

    def add_edge(self, from_node, to_node, cost):
        # Add a directed edge with cost between two nodes
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, cost))

    def get_neighbors(self, node_id):
        # Return all neighboring nodes and edge costs
        return self.edges.get(node_id, [])

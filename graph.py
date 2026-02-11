import math

class Graph:
    def __init__(self):
        # Store node coordinates
        self.nodes = {}
        
        # Store adjacency list with edge costs
        self.edges = {}

    def add_node(self, node_id, coordinates):
        # Add node with coordinates
        self.nodes[node_id] = coordinates

    def add_edge(self, u, v, cost):
        # Add directed edge u -> v with cost
        if u not in self.edges:
            self.edges[u] = {}
        self.edges[u][v] = cost

    def get_neighbors(self, node_id):
        # Return neighbors of node
        if node_id in self.edges:
            return list(self.edges[node_id].keys())
        return []

    def get_cost(self, u, v):
        # Return edge cost from u to v
        if u in self.edges and v in self.edges[u]:
            return self.edges[u][v]
        return float('inf')

    def get_coordinates(self, node_id):
        # Return node coordinates
        return self.nodes.get(node_id)

    def get_heuristic(self, u, v):
        # Euclidean distance heuristic
        if u not in self.nodes or v not in self.nodes:
            return float('inf')
        
        x1, y1 = self.nodes[u]
        x2, y2 = self.nodes[v]
        
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

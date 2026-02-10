import math

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node_id, coord):
        self.nodes[node_id] = coord
        if node_id not in self.edges:
            self.edges[node_id] = []

    def add_edge(self, src, dst, cost):
        if src not in self.edges:
            self.edges[src] = []
        self.edges[src].append((dst, cost))

    def neighbors(self, node_id):
        return self.edges.get(node_id, [])

    # Heuristic: Euclidean distance to the nearest destination
    def heuristic(self, node_id, destinations):
        x1, y1 = self.nodes[node_id]
        return min(
            math.sqrt((x1 - self.nodes[d][0]) ** 2 + (y1 - self.nodes[d][1]) ** 2)
            for d in destinations
        )

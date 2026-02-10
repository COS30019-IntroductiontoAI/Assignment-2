import heapq

class GBFS:
    def __init__(self, graph, origin, destinations):
        self.graph = graph
        self.origin = origin
        self.destinations = destinations
        self.nodes_created = 0

    # Greedy Best-First Search
    def search(self):
        frontier = []
        order = 0

        heapq.heappush(
            frontier,
            (self.graph.heuristic(self.origin, self.destinations),
             order,
             self.origin,
             [self.origin])
        )
        self.nodes_created += 1

        visited = set()

        while frontier:
            _, _, current, path = heapq.heappop(frontier)

            if current in visited:
                continue
            visited.add(current)

            # Goal test
            if current in self.destinations:
                return current, self.nodes_created, path

            # Node expansion
            for neighbor, _ in sorted(self.graph.neighbors(current)):
                if neighbor not in visited:
                    order += 1
                    heapq.heappush(
                        frontier,
                        (self.graph.heuristic(neighbor, self.destinations),
                         order,
                         neighbor,
                         path + [neighbor])
                    )
                    self.nodes_created += 1

        return None, self.nodes_created, []
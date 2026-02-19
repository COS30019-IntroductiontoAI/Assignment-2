import heapq
import math

# Independent heuristic function (Euclidean distance)
def calculate_heuristic(graph, node_id, goal_ids):
    try:
        # Get coordinates if graph contains nodes dictionary
        if hasattr(graph, 'nodes') and node_id in graph.nodes:
            node = graph.nodes[node_id]
            min_distance = float('inf')
            
            for goal_id in goal_ids:
                if goal_id in graph.nodes:
                    goal = graph.nodes[goal_id]
                    # Safely get x, y coordinates
                    nx = getattr(node, 'x', 0)
                    ny = getattr(node, 'y', 0)
                    gx = getattr(goal, 'x', 0)
                    gy = getattr(goal, 'y', 0)
                    
                    # Calculate straight-line (Euclidean) distance
                    e_distance = math.sqrt((nx - gx) ** 2 + (ny - gy) ** 2)
                    if e_distance < min_distance:
                        min_distance = e_distance
            return min_distance if min_distance != float('inf') else 0
    except Exception:
        pass
    return 0

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

        # Push to heap: (Heuristic, order, node_id, path, current_cost)
        heapq.heappush(
            frontier,
            (calculate_heuristic(self.graph, self.origin, self.destinations),
            int(self.origin),
            order,
            self.origin,
            [self.origin],
            0)
        )

        self.nodes_created += 1

        visited = set()

        while frontier:
            # Pop the node with the smallest heuristic from the queue
            h_val, _, current, path, current_cost = heapq.heappop(frontier)

            if current in visited:
                continue
            visited.add(current)

            # Goal test
            if current in self.destinations:
                # Return in the format required by search.py: path, node_count, total_cost
                return path, self.nodes_created, current_cost

            # Get adjacency list (Supports both get_neighbors or neighbors methods)
            if hasattr(self.graph, 'get_neighbors'):
                neighbors_raw = self.graph.get_neighbors(current)
            elif hasattr(self.graph, 'neighbors'):
                neighbors_raw = self.graph.neighbors(current)
            else:
                neighbors_raw = []
                
            # Node expansion (Ensure sorting for deterministic results)
            if neighbors_raw and isinstance(neighbors_raw[0], tuple):
                neighbors_raw.sort(key=lambda x: int(x[0]))
            else:
                neighbors_raw.sort(key=lambda x: int(x))

            for item in neighbors_raw:
                if isinstance(item, tuple):
                    neighbor = item[0]
                    step_cost = item[1]
                else:
                    neighbor = item
                    step_cost = 0

                if neighbor not in visited:
                    order += 1
                    heapq.heappush(
                        frontier,
                        (calculate_heuristic(self.graph, neighbor, self.destinations),
                        int(neighbor),
                        order,
                        neighbor,
                        path + [neighbor],
                        current_cost + step_cost)
                    )

                    self.nodes_created += 1

        return [], self.nodes_created, 0
    
def gbfs(graph, start_id, goal_ids):
    solver = GBFS(graph, start_id, goal_ids)
    return solver.search()
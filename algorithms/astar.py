import heapq
from utils import heuristic, reconstruct_path


class SearchNode:
    """
    Represents a node in the SEARCH TREE.

    IMPORTANT:
    - This is NOT a graph node
    - Multiple SearchNodes may refer to the same graph state
    """

    def __init__(self, state, parent, g_cost, h_cost, insertion_order):
        self.state = state            # graph node ID
        self.parent = parent          # parent SearchNode
        self.g = g_cost               # cost from origin to this node
        self.h = h_cost               # heuristic estimate to goal
        self.f = g_cost + h_cost      # evaluation function
        self.order = insertion_order # used for tie-breaking

    def __lt__(self, other):
        """
        Priority comparison for the frontier (min-heap).

        Tie-breaking rules:
        1. Smaller f(n)
        2. Smaller node ID
        3. Earlier insertion order
        """
        return (self.f, self.state, self.order) < (other.f, other.state, other.order)


def astar_search(graph, origin, destinations):
    """
    Perform tree-based A* search.

    Rules strictly follow the assignment:
    - No closed list
    - No cost update
    - Stop when ANY destination is reached
    """

    frontier = []                    # priority queue of SearchNodes
    generated_node_count = 0         # counts ALL generated search nodes
    insertion_order = 0              # ensures deterministic expansion order

    # Create the root of the search tree
    start_node = SearchNode(
        state=origin,
        parent=None,
        g_cost=0,
        h_cost=heuristic(graph.nodes[origin], graph, destinations),
        insertion_order=insertion_order
    )

    heapq.heappush(frontier, start_node)
    generated_node_count += 1

    # Main search loop
    while frontier:
        current_node = heapq.heappop(frontier)

        # Goal test: stop immediately when a destination is reached
        if current_node.state in destinations:
            return (
                current_node.state,
                generated_node_count,
                reconstruct_path(current_node)
            )

        # Expand current node (tree-based: always generate new nodes)
        for (child_state, cost) in graph.adjacency[current_node.state]:
            insertion_order += 1

            child_g = current_node.g + cost
            child_h = heuristic(graph.nodes[child_state], graph, destinations)

            child_node = SearchNode(
                state=child_state,
                parent=current_node,
                g_cost=child_g,
                h_cost=child_h,
                insertion_order=insertion_order
            )

            heapq.heappush(frontier, child_node)
            generated_node_count += 1

    # No destination reachable
    return None, generated_node_count, []

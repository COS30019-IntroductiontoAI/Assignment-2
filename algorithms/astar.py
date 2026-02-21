import heapq
from utils import heuristic, reconstruct_path


def is_state_in_ancestor_chain(node, state):
    # Return True if state already exists on current path
    # from root to the current node.
    current = node
    while current is not None:
        if current.state == state:
            return True
        current = current.parent
    return False


class SearchNode:
    # Search-tree node used in the frontier heap.
    # Different SearchNodes may reference the same graph state.

    def __init__(self, state, parent, g_cost, h_cost, insertion_order):
        self.state = state            # graph node ID
        self.parent = parent          # parent SearchNode
        self.g = g_cost               # cost from origin to this node
        self.h = h_cost               # heuristic estimate to goal
        self.f = g_cost + h_cost      # evaluation function
        self.order = insertion_order  # used for tie-breaking

    def __lt__(self, other):
        # Heap priority uses strict tie-break order.
        # Compare by f(n), then state id, then insertion order.
        return (self.f, self.state, self.order) < (other.f, other.state, other.order)


def astar_search(graph, origin, destinations):
    # Tree-based A*: no closed list, no global cost updates.
    # Stop at first goal popped; avoid only branch-local cycles.

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
                reconstruct_path(current_node),
                generated_node_count,
                current_node.g
            )
            
        # Read outgoing edges for current state.
        # Keep fallbacks for compatible graph interfaces.
        if hasattr(graph, 'get_neighbors'):
            neighbors_raw = graph.get_neighbors(current_node.state)
        elif hasattr(graph, 'neighbors'):
            neighbors_raw = graph.neighbors(current_node.state)
        else:
            try:
                neighbors_raw = graph.edges.get(current_node.state, [])
            except Exception:
                neighbors_raw = []

        # Enforce deterministic expansion order required by spec.
        # Smaller node id is expanded first when other factors tie.
        if neighbors_raw and isinstance(neighbors_raw[0], tuple):
            neighbors_raw.sort(key=lambda x: int(x[0]))
        else:
            neighbors_raw.sort(key=lambda x: int(x))

        # Generate children in ascending node-id order.
        for item in neighbors_raw:
            # Graph format is usually (neighbor, edge_cost).
            # The else path keeps compatibility with other layouts.
            if isinstance(item, tuple):
                child_state = item[0]
                cost = item[1]
            else:
                child_state = item
                cost = 0
                if hasattr(graph, 'cost') and graph.cost is not None:
                    cost = graph.cost.get((current_node.state, child_state), 0)

            # Skip states already on the current branch.
            if is_state_in_ancestor_chain(current_node, child_state):
                continue

            # Evaluate child using standard A* score: f = g + h.
            # g is real path cost, h estimates distance to nearest goal.
            child_g = current_node.g + cost
            child_h = heuristic(graph.nodes[child_state], graph, destinations)

            # Increase order only when a child is actually generated.
            # This preserves chronological tie-break among equal priorities.
            insertion_order += 1
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
    return [], generated_node_count, 0

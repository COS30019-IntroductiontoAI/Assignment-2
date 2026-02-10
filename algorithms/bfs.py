from collections import deque

def bfs(graph, start_node, goal_nodes):
    queue = deque([start_node])
    visited = set([start_node])
    came_from = {start_node: None}
    explored_count = 0

    while queue:
        current_node = queue.popleft()
        explored_count += 1
        
        # Kiểm tra đích
        if current_node in goal_nodes:
            path = reconstruct_path(came_from, current_node)
            return current_node, explored_count, path
        
        #Lấy danh sách láng giềng từ Graph
        neighbors = graph.get_neighbors(current_node)
        
        # Sắp xếp tăng dần theo ID (ép kiểu int để so sánh đúng số học)
        neighbors.sort(key=lambda x: int(x))
        
        for next_node in neighbors:
            if next_node not in visited:
                visited.add(next_node)
                came_from[next_node] = current_node # Lưu cha
                queue.append(next_node)

    return None, explored_count, [] # Không tìm thấy đường đi

def reconstruct_path(came_from, current):
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse() # Đảo ngược lại để có đường đi từ Start -> Goal
    return path
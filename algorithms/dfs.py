# algorithms/dfs.py

def dfs(graph, start_node, goal_nodes):

    # 1 Tạo Stack với start node 
    stack = [start_node]
    
    # Tập hợp các node đã thăm để tránh chu trình (cycles)
    visited = set()
    
    # Lưu vết đường đi: Key=Con, Value=Cha
    came_from = {start_node: None}
    
    explored_count = 0

    while stack:
        # 2 Lấy node từ đỉnh Stack (LIFO)
        current_node = stack.pop()
        
        # Nếu node này đã được xử lý rồi thì bỏ qua (trường hợp node nằm nhiều lần trong stack)
        if current_node in visited:
            continue
            
        # Đánh dấu đã thăm
        visited.add(current_node)
        explored_count += 1
        
        # 3 Kiểm tra đích
        if current_node in goal_nodes:
            path = reconstruct_path(came_from, current_node)
            return current_node, explored_count, path

        # 4 Lấy láng giềng và thêm vào Stack
        neighbors = graph.get_neighbors(current_node)
        
        # Sắp xếp GIẢM DẦN
        # Vì Stack là LIFO, để duyệt node NHỎ trước
        # Khi pop(), node NHỎ sẽ được lấy ra trước.
        neighbors.sort(key=lambda x: int(x), reverse=True)
        
        for next_node in neighbors:
            if next_node not in visited:
                if next_node not in came_from:
                    came_from[next_node] = current_node
                stack.append(next_node)

    return None, explored_count, []

def reconstruct_path(came_from, current):
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path
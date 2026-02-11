# search.py
import sys
from graph import Graph
import parser
# Import các thuật toán
from algorithms.bfs import bfs
from algorithms.dfs import dfs  # Bạn sẽ bỏ comment dòng này khi viết xong dfs.py

def main():
    # 1. Kiểm tra tham số dòng lệnh
    # Format: python search.py <filename> <method>
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        return

    filename = sys.argv[1]
    method = sys.argv[2].upper() # Chuyển thành chữ hoa để dễ so sánh (BFS, bfs -> BFS)

    # 2. Khởi tạo đồ thị và đọc dữ liệu
    graph = Graph()
    origin, destinations = parser.read_file(filename, graph)

    if origin is None:
        return # Lỗi đọc file

    # 3. Chọn thuật toán dựa trên tham số 'method'
    result = None
    
    if method == "BFS":
        # Gọi hàm bfs từ file algorithms/bfs.py
        # Trả về: (goal_node, explored_count, path)
        result = bfs(graph, origin, destinations)
        
    elif method == "DFS":
        result = dfs(graph, origin, destinations)
        # print("DFS has not been implemented yet.")
        # return
    else:
        print(f"Method {method} not supported.")
        return

    # 4. In kết quả theo đúng định dạng đề bài yêu cầu
    # Format: filename method
    #         goal number_of_nodes path
    goal_node, num_nodes, path = result

    print(f"{filename} {method}")
    
    if goal_node:
        # Chuyển list path ['2', '1', '4'] thành chuỗi "2 1 4"
        path_str = " ".join(path) 
        print(f"{goal_node} {num_nodes} {path_str}")
    else:
        print(f"No path found. Nodes visited: {num_nodes}")

if __name__ == "__main__":
    main()
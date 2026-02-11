import math

class Graph:
    def __init__(self):
        """
        Khởi tạo đồ thị.
        - self.nodes: Lưu tọa độ của các node. Ví dụ: {'1': (4, 1), '2': (2, 2)}
        - self.edges: Lưu danh sách kề và chi phí. Sử dụng dict lồng nhau để truy cập nhanh.
                      Ví dụ: {'2': {'1': 4, '3': 5}} nghĩa là từ 2 sang 1 mất 4, từ 2 sang 3 mất 5.
        """
        self.nodes = {} 
        self.edges = {}

    def add_node(self, node_id, coordinates):
        """
        Thêm một node và tọa độ của nó vào đồ thị.
        Args:
            node_id (str): ID của node (ví dụ: '1').
            coordinates (tuple): Tọa độ (x, y).
        """
        self.nodes[node_id] = coordinates

    def add_edge(self, u, v, cost):
        """
        Thêm một cạnh có hướng từ u đến v với chi phí cost.
        Lưu ý: Đề bài mô tả đồ thị có hướng (mũi tên).
        """
        if u not in self.edges:
            self.edges[u] = {}
        self.edges[u][v] = cost

    def get_neighbors(self, node_id):
        """
        Lấy danh sách các node kề (neighbors) mà node_id có thể đi tới.
        Dùng cho: BFS, DFS.
        """
        if node_id in self.edges:
            # Trả về danh sách các keys (các node đích)
            # Lưu ý: Việc sort sẽ được thực hiện ở thuật toán tìm kiếm (BFS/DFS)
            return list(self.edges[node_id].keys())
        return []

    def get_cost(self, u, v):
        """
        Lấy chi phí đi từ u đến v.
        Dùng cho: Uniform Cost Search, A*.
        """
        if u in self.edges and v in self.edges[u]:
            return self.edges[u][v]
        return float('inf') # Nếu không có cạnh nối, chi phí là vô cực

    def get_coordinates(self, node_id):
        """Lấy tọa độ của một node."""
        return self.nodes.get(node_id)

    def get_heuristic(self, u, v):
        """
        Tính khoảng cách Euclid giữa 2 node u và v.
        Hàm này rất quan trọng cho thuật toán A* (A Star) và GBFS sau này.
        Công thức: căn bậc hai của ((x1-x2)^2 + (y1-y2)^2).
        """
        if u not in self.nodes or v not in self.nodes:
            return float('inf')
        
        x1, y1 = self.nodes[u]
        x2, y2 = self.nodes[v]
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
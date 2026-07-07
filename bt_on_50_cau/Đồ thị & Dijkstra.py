import heapq

# --- CÂU 15: DIJKSTRA CƠ BẢN ---
def dijkstra_co_ban(do_thi, nguon):
    # Sử dụng danh sách kề để biểu diễn đồ thị
    khoang_cach = {dinh: float('inf') for dinh in do_thi}
    khoang_cach[nguon] = 0
    chua_duyet = list(do_thi.keys())
    
    while chua_duyet:
        # Tìm đỉnh có khoảng cách nhỏ nhất trong số các đỉnh chưa duyệt
        u = min(chua_duyet, key=lambda x: khoang_cach[x])
        chua_duyet.remove(u)
        
        if khoang_cach[u] == float('inf'):
            break
            
        for ke, trong_so in do_thi.get(u, []):
            kc_moi = khoang_cach[u] + trong_so
            if kc_moi < khoang_cach[ke]:
                khoang_cach[ke] = kc_moi
                
    return khoang_cach

do_thi_mau = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print("Cau 15: ", dijkstra_co_ban(do_thi_mau, 0))


# --- CÂU 16: TRUY VẾT ĐƯỜNG ĐI ---
def dijkstra_truy_vet(do_thi, nguon, dich):
    khoang_cach = {dinh: float('inf') for dinh in do_thi}
    cha = {dinh: None for dinh in do_thi}
    khoang_cach[nguon] = 0
    
    hq = [(0, nguon)]
    
    while hq:
        kc_u, u = heapq.heappop(hq)
        if kc_u > khoang_cach[u]: 
            continue
            
        for ke, trong_so in do_thi.get(u, []):
            kc_moi = kc_u + trong_so
            if kc_moi < khoang_cach[ke]:
                khoang_cach[ke] = kc_moi
                cha[ke] = u
                heapq.heappush(hq, (kc_moi, ke))
                
    duong_di = []
    hien_tai = dich
    while hien_tai is not None:
        duong_di.append(hien_tai)
        hien_tai = cha[hien_tai]
    duong_di.reverse()
    
    return duong_di if duong_di[0] == nguon else []

print("Cau 16: ", dijkstra_truy_vet(do_thi_mau, 0, 3))


# --- CÂU 17: DIJKSTRA VỚI HEAP ---
def dijkstra_voi_heap(do_thi, nguon):
    # Đạt độ phức tạp O((V + E) log V), phù hợp đồ thị thưa
    khoang_cach = {dinh: float('inf') for dinh in do_thi}
    khoang_cach[nguon] = 0
    
    hq = [(0, nguon)]
    
    while hq:
        kc_u, u = heapq.heappop(hq)
        
        if kc_u > khoang_cach[u]:
            continue
            
        for ke, trong_so in do_thi.get(u, []):
            kc_moi = kc_u + trong_so
            if kc_moi < khoang_cach[ke]:
                khoang_cach[ke] = kc_moi
                heapq.heappush(hq, (kc_moi, ke))
                
    return khoang_cach

print("Cau 17: ", dijkstra_voi_heap(do_thi_mau, 0))


# --- CÂU 18: VÌ SAO CẦN TRỌNG SỐ KHÔNG ÂM ---
def giai_thich_dijkstra_canh_am():
    # Giải thích bước "chốt đỉnh" bị phá vỡ:
    # Dijkstra hoạt động theo cơ chế tham lam. Khi một đỉnh có khoảng cách nhỏ nhất được lấy ra khỏi 
    # hàng đợi, thuật toán coi như đường đi ngắn nhất đến đỉnh đó đã tối ưu và không thay đổi (chốt đỉnh).
    # Tuy nhiên, nếu đồ thị có cạnh âm, một đường đi vòng qua cạnh âm có thể xuất hiện muộn hơn nhưng 
    # lại có tổng chi phí nhỏ hơn đường đi đã chốt, làm cho kết quả của Dijkstra bị sai.
    # Thuật toán thay thế khi có cạnh âm: Bellman-Ford hoặc định lý Johnson.
    pass


# --- CÂU 19: ĐƯỜNG ĐI NGẮN NHẤT TRÊN LƯỚI ---
def dijkstra_tren_luoi(ma_tran_chi_phi):
    R = len(ma_tran_chi_phi)
    C = len(ma_tran_chi_phi[0])
    
    khoang_cach = [[float('inf')] * C for _ in range(R)]
    khoang_cach[0][0] = ma_tran_chi_phi[0][0]
    
    hq = [(ma_tran_chi_phi[0][0], 0, 0)]
    huong_di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while hq:
        cp_hien_tai, r, c = heapq.heappop(hq)
        
        if r == R - 1 and c == C - 1:
            return cp_hien_tai
            
        if cp_hien_tai > khoang_cach[r][c]:
            continue
            
        for dr, dc in huong_di:
            n_r, n_c = r + dr, c + dc
            if 0 <= n_r < R and 0 <= n_c < C:
                cp_moi = cp_hien_tai + ma_tran_chi_phi[n_r][n_c]
                if cp_moi < khoang_cach[n_r][n_c]:
                    khoang_cach[n_r][n_c] = cp_moi
                    heapq.heappush(hq, (cp_moi, n_r, n_c))
    return -1

luoi_chi_phi = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print("Cau 19: ", dijkstra_tren_luoi(luoi_chi_phi))


# --- CÂU 20: DIJKSTRA VS BELLMAN-FORD VS A* ---
# So sánh điều kiện áp dụng, độ phức tạp và vai trò heuristic:
#Dijkstra áp dụng cho đồ thị có trọng số không âm, chạy nhanh với độ phức tạp $O((V + E) \log V)$ nhờ cơ chế tham lam (Min-Heap), nhưng hoàn toàn bất lực và cho kết quả sai nếu đồ thị có cạnh âm vì bước chốt đỉnh bị phá vỡ.
#Bellman-Ford giải quyết được điểm yếu của Dijkstra khi chấp nhận cả cạnh có trọng số âm và có khả năng phát hiện chu trình âm, đổi lại tốc độ chạy chậm hơn nhiều với độ phức tạp $O(V \times E)$ do phải duyệt lặp toàn bộ các cạnh.
#A* là bản nâng cấp của Dijkstra để tìm đường đến một đích cụ thể, vẫn yêu cầu trọng số không âm nhưng tích hợp thêm hàm Heuristic giúp định hướng không gian tìm kiếm, giảm số lượng đỉnh phải duyệt để tăng tốc độ xử lý.
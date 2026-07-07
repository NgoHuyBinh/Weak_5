from collections import deque

# --- CÂU 26
class CircularQueue:
    def __init__(self, dung_luong):
        self.dung_luong = dung_luong
        self.mang = [None] * dung_luong
        self.dau = -1
        self.cuoi = -1

    def enqueue(self, gia_tri):
        if (self.cuoi + 1) % self.dung_luong == self.dau:
            return False  # Hàng đợi đầy
        elif self.dau == -1:
            self.dau = 0
            self.cuoi = 0
            self.mang[self.cuoi] = gia_tri
        else:
            self.cuoi = (self.cuoi + 1) % self.dung_luong
            self.mang[self.cuoi] = gia_tri
        return True

    def dequeue(self):
        if self.dau == -1:
            return None  # Hàng đợi rỗng
        gia_tri_tra_ve = self.mang[self.dau]
        if self.dau == self.cuoi:
            self.dau = -1
            self.cuoi = -1
        else:
            self.dau = (self.dau + 1) % self.dung_luong
        return gia_tri_tra_ve

q_26 = CircularQueue(5)
q_26.enqueue(1)
q_26.enqueue(2)
print("Cau 26: ", q_26.dequeue())


# --- CÂU 27
class QueueUsingTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, gia_tri):
        self.in_stack.append(gia_tri)

    def dequeue(self):
        # Chi phí trích xuất trung bình (amortized) đạt O(1)
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop() if self.out_stack else None

q_27 = QueueUsingTwoStacks()
q_27.enqueue(1)
q_27.enqueue(2)
print("Cau 27: ", q_27.dequeue())


# --- CÂU 28
def bfs_do_thi(do_thi, nut_nguon):
    da_tham = set([nut_nguon])
    hang_doi = deque([nut_nguon])
    thu_tu_tham = []
    
    while hang_doi:
        u = hang_doi.popleft()
        thu_tu_tham.append(u)
        
        for ke in do_thi.get(u, []):
            if ke not in da_tham:
                da_tham.add(ke)
                hang_doi.append(ke)
                
    return thu_tu_tham

do_thi_mau = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
print("Cau 28: ", bfs_do_thi(do_thi_mau, 2))


# --- CÂU 29
def max_cua_so_truot(mang, k):
    if not mang or k <= 0:
        return []
    
    ket_qua = []
    dq = deque()  # Lưu trữ chỉ số (index), đảm bảo giá trị giảm dần đơn điệu
    
    for i in range(len(mang)):
        # Loại bỏ các phần tử nằm ngoài cửa sổ hiện tại
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        # Loại bỏ các phần tử nhỏ hơn phần tử hiện tại sắp được chèn vào
        while dq and mang[dq[-1]] < mang[i]:
            dq.pop()
            
        dq.append(i)
        
        # Ghi nhận kết quả khi cửa sổ đã đạt đủ kích thước k
        if i >= k - 1:
            ket_qua.append(mang[dq[0]])
            
    return ket_qua

mang_29 = [1, 3, -1, -3, 5, 3]
print("Cau 29: ", max_cua_so_truot(mang_29, 3))


# --- CÂU 30
def mo_phong_round_robin(cac_tien_trinh, quantum):
    # cac_tien_trinh: danh sach cac cap [ten_tien_trinh, thoi_gian_chay]
    hang_doi = deque(cac_tien_trinh)
    thoi_gian_hien_tai = 0
    thoi_diem_hoan_thanh = {}
    
    while hang_doi:
        ten, tg_con_lai = hang_doi.popleft()
        
        if tg_con_lai <= quantum:
            thoi_gian_hien_tai += tg_con_lai
            thoi_diem_hoan_thanh[ten] = thoi_gian_hien_tai
        else:
            thoi_gian_hien_tai += quantum
            hang_doi.append([ten, tg_con_lai - quantum])
            
    return thoi_diem_hoan_thanh

ds_tien_trinh = [["P1", 5], ["P2", 2], ["P3", 4]]
print("Cau 30: ", mo_phong_round_robin(ds_tien_trinh, 2))
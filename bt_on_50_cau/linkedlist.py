class Nut:
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.tiep_theo = None


# --- CÂU 36
class DanhSachDaoNguoc:
    def __init__(self):
        self.dau = None

    def pushBack(self, gia_tri):
        nut_moi = Nut(gia_tri)
        if not self.dau:
            self.dau = nut_moi
            return
        hien_tai = self.dau
        while hien_tai.tiep_theo:
            hien_tai = hien_tai.tiep_theo
        hien_tai.tiep_theo = nut_moi

    def dao_nguoc_lap(self):
        # Kỹ thuật dùng 3 con trỏ
        truoc = None
        hien_tai = self.dau
        while hien_tai:
            sau = hien_tai.tiep_theo
            hien_tai.tiep_theo = truoc
            truoc = hien_tai
            hien_tai = sau
        self.dau = truoc

    def _dao_nguoc_de_quy_helper(self, hien_tai, truoc=None):
        if not hien_tai:
            return truoc
        sau = hien_tai.tiep_theo
        hien_tai.tiep_theo = truoc
        return self._dao_nguoc_de_quy_helper(sau, hien_tai)

    def dao_nguoc_de_quy(self):
        self.dau = self._dao_nguoc_de_quy_helper(self.dau)

    def in_toan_bo(self):
        chuoi_kq = []
        hien_tai = self.dau
        while hien_tai:
            chuoi_kq.append(str(hien_tai.du_lieu))
            hien_tai = hien_tai.tiep_theo
        chuoi_kq.append("null")
        return "->".join(chuoi_kq)

ds_36 = DanhSachDaoNguoc()
ds_36.pushBack(1)
ds_36.pushBack(2)
ds_36.pushBack(3)
ds_36.dao_nguoc_lap()
print("Cau 36 (Lap): ", ds_36.in_toan_bo())


# --- CÂU 37
def tim_nut_giua(dau_nut):
    # Kỹ thuật con trỏ nhanh / chậm trong một lượt duyệt
    chom = dau_nut
    nhanh = dau_nut
    while nhanh and nhanh.tiep_theo:
        chom = chom.tiep_theo
        nhanh = nhanh.tiep_theo.tiep_theo
    return chom.du_lieu if chom else None

n37_1 = Nut(1)
n37_2 = Nut(2)
n37_3 = Nut(3)
n37_1.tiep_theo = n37_2
n37_2.tiep_theo = n37_3
print("Cau 37: ", tim_nut_giua(n37_1))


# --- CÂU 38
def tim_dau_chu_trinh_floyd(dau_nut):
    rua = dau_nut
    tho = dau_nut
    co_chu_trinh = False
    
    # Phát hiện chu trình (Rùa và Thỏ)
    while tho and tho.tiep_theo:
        rua = rua.tiep_theo
        tho = tho.tiep_theo.tiep_theo
        if rua == tho:
            co_chu_trinh = True
            break
            
    if not co_chu_trinh:
        return None
        
    # Tìm nút bắt đầu chu trình
    rua = dau_nut
    while rua != tho:
        rua = rua.tiep_theo
        tho = tho.tiep_theo
        
    return rua.du_lieu

n38_1 = Nut(1)
n38_2 = Nut(2)
n38_3 = Nut(3)
n38_1.tiep_theo = n38_2
n38_2.tiep_theo = n38_3
n38_3.tiep_theo = n38_2  # Tạo chu trình quay lại nút 2
print("Cau 38: ", tim_dau_chu_trinh_floyd(n38_1))


# --- CÂU 39
def xoa_nut_k_tu_cuoi(dau_nut, k):
    nut_gia = Nut(0)
    nut_gia.tiep_theo = dau_nut
    nhanh = nut_gia
    chom = nut_gia
    
    # Cho con trỏ nhanh tiến trước k + 1 bước để tạo khoảng cách k
    for _ in range(k + 1):
        nhanh = nhanh.tiep_theo
        
    # Duyệt cả hai con trỏ dịch chuyển đồng tốc cùng nhau
    while nhanh:
        nhanh = nhanh.tiep_theo
        chom = chom.tiep_theo
        
    # chom hiện tại nằm ngay trước nút cần xóa
    chom.tiep_theo = chom.tiep_theo.tiep_theo
    return nut_gia.tiep_theo

n39_1 = Nut(1)
n39_2 = Nut(2)
n39_3 = Nut(3)
n39_1.tiep_theo = n39_2
n39_2.tiep_theo = n39_3
kq_39 = xoa_nut_k_tu_cuoi(n39_1, 2)
print("Cau 39 (Xoa nut thu 2 tu cuoi): ", kq_39.du_lieu if kq_39 else None)


# --- CÂU 40
def lay_nut_giua_de_cat(dau_nut):
    if not dau_nut:
        return dau_nut
    chom = dau_nut
    nhanh = dau_nut
    while nhanh.tiep_theo and nhanh.tiep_theo.tiep_theo:
        chom = chom.tiep_theo
        nhanh = nhanh.tiep_theo.tiep_theo
    return chom

def tron_hai_danh_sach(l1, l2):
    nut_gia = Nut(0)
    hien_tai = nut_gia
    while l1 and l2:
        if l1.du_lieu <= l2.du_lieu:
            hien_tai.tiep_theo = l1
            l1 = l1.tiep_theo
        else:
            hien_tai.tiep_theo = l2
            l2 = l2.tiep_theo
        hien_tai = hien_tai.tiep_theo
    if l1: hien_tai.tiep_theo = l1
    if l2: hien_tai.tiep_theo = l2
    return nut_gia.tiep_theo

def merge_sort_linked_list(dau_nut):
    if not dau_nut or not dau_nut.tiep_theo:
        return dau_nut
        
    giua = lay_nut_giua_de_cat(dau_nut)
    sau_giua = giua.tiep_theo
    giua.tiep_theo = None  # Tách đôi danh sách
    
    trai = merge_sort_linked_list(dau_nut)
    phai = merge_sort_linked_list(sau_giua)
    
    return tron_hai_danh_sach(trai, phai)

n40_1 = Nut(3)
n40_2 = Nut(1)
n40_3 = Nut(2)
n40_1.tiep_theo = n40_2
n40_2.tiep_theo = n40_3
kq_40 = merge_sort_linked_list(n40_1)
print("Cau 40: ", kq_40.du_lieu, "->", kq_40.tiep_theo.du_lieu)


# --- CÂU 41
class NutDoi:
    def __init__(self, khoa, gia_tri):
        self.khoa = khoa
        self.gia_tri = gia_tri
        self.truoc = None
        self.tiep_theo = None

class LRUCache:
    def __init__(self, dung_luong):
        self.dung_luong = dung_luong
        self.ban_do = {}  # Bảng băm lưu giữ {khoa: NutDoi}
        
        # Tạo nút giả đầu cuối cho danh sách liên kết đôi (Doubly Linked List)
        self.dau = NutDoi(0, 0)
        self.cuoi = NutDoi(0, 0)
        self.dau.tiep_theo = self.cuoi
        self.cuoi.truoc = self.dau

    def _xoa_nut(self, nut):
        nut.truoc.tiep_theo = nut.tiep_theo
        nut.tiep_theo.truoc = nut.truoc

    def _them_vao_dau(self, nut):
        nut.tiep_theo = self.dau.tiep_theo
        nut.tiep_theo.truoc = nut
        self.dau.tiep_theo = nut
        nut.truoc = self.dau

    def get(self, khoa):
        if khoa in self.ban_do:
            nut = self.ban_do[khoa]
            self._xoa_nut(nut)
            self._them_vao_dau(nut)  # Đẩy phần tử mới nhất lên đầu
            return nut.gia_tri
        return -1

    def put(self, khoa, gia_tri):
        if khoa in self.ban_do:
            self._xoa_nut(self.ban_do[khoa])
        nut_moi = NutDoi(khoa, gia_tri)
        self._them_vao_dau(nut_moi)
        self.ban_do[khoa] = nut_moi
        
        if len(self.ban_do) > self.dung_luong:
            nut_duoi_cuoi = self.cuoi.truoc
            self._xoa_nut(nut_duoi_cuoi)
            del self.ban_do[nut_duoi_cuoi.khoa]

cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
print("Cau 41 (Lay khoa 1): ", cache.get(1))
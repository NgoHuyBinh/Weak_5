# --- BÀI 11
class NutDoi:
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.truoc = None
        self.tiep_theo = None

class DanhSachLienKetDoi:
    def __init__(self):
        self.dau = None
        self.cuoi = None

    def pushFront(self, gia_tri):
        nut_moi = NutDoi(gia_tri)
        if not self.dau:
            self.dau = nut_moi
            self.cuoi = nut_moi
        else:
            nut_moi.tiep_theo = self.dau
            self.dau.truoc = nut_moi
            self.dau = nut_moi

    def pushBack(self, gia_tri):
        nut_moi = NutDoi(gia_tri)
        if not self.cuoi:
            self.dau = nut_moi
            self.cuoi = nut_moi
        else:
            nut_moi.truoc = self.cuoi
            self.cuoi.tiep_theo = nut_moi
            self.cuoi = nut_moi

    def duyet_xuoi(self):
        kq = []
        hien_tai = self.dau
        while hien_tai:
            kq.append(str(hien_tai.du_lieu))
            hien_tai = hien_tai.tiep_theo
        return "->".join(kq)

    def duyet_nguoc(self):
        kq = []
        hien_tai = self.cuoi
        while hien_tai:
            kq.append(str(hien_tai.du_lieu))
            hien_tai = hien_tai.truoc
        return "->".join(kq)

ds_bai_11 = DanhSachLienKetDoi()
ds_bai_11.pushFront(1)
ds_bai_11.pushBack(2)
ds_bai_11.pushBack(3)
print("Bai 11: ", f"Xuoi: {ds_bai_11.duyet_xuoi()} | Nguoc: {ds_bai_11.duyet_nguoc()}")


# --- BÀI 12
class NutBai12:
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.tiep_theo = None

def tim_bat_dau_chu_trinh(dau_nut):
    rua = dau_nut
    tho = dau_nut
    co_chu_trinh = False
    
    while tho and tho.tiep_theo:
        rua = rua.tiep_theo
        tho = tho.tiep_theo.tiep_theo
        if rua == tho:
            co_chu_trinh = True
            break
            
    if not co_chu_trinh:
        return None
        
    rua = dau_nut
    while rua != tho:
        rua = rua.tiep_theo
        tho = tho.tiep_theo
        
    return rua.du_lieu

n1 = NutBai12(1)
n2 = NutBai12(2)
n3 = NutBai12(3)
n1.tiep_theo = n2
n2.tiep_theo = n3
n3.tiep_theo = n2
print("Bai 12: ", tim_bat_dau_chu_trinh(n1))


# --- BÀI 13
class NutBai13:
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.tiep_theo = None

def lay_nut_giua(dau_nut):
    if not dau_nut:
        return dau_nut
    chong = dau_nut
    nhanh = dau_nut
    while nhanh.tiep_theo and nhanh.tiep_theo.tiep_theo:
        chong = chong.tiep_theo
        nhanh = nhanh.tiep_theo.tiep_theo
    return chong

def tron_hai_danh_sach(l1, l2):
    nut_gia = NutBai13(0)
    hien_tai = nut_gia
    while l1 and l2:
        if l1.du_lieu <= l2.du_lieu:
            hien_tai.tiep_theo = l1
            l1 = l1.tiep_theo
        else:
            hien_tai.tiep_theo = l2
            l2 = l2.tiep_theo
        hien_tai = hien_tai.tiep_theo
    if l1:
        hien_tai.tiep_theo = l1
    if l2:
        hien_tai.tiep_theo = l2
    return nut_gia.tiep_theo

def merge_sort_linked_list(dau_nut):
    if not dau_nut or not dau_nut.tiep_theo:
        return dau_nut
    giua = lay_nut_giua(dau_nut)
    sau_giua = giua.tiep_theo
    giua.tiep_theo = None
    trai = merge_sort_linked_list(dau_nut)
    phai = merge_sort_linked_list(sau_giua)
    return tron_hai_danh_sach(trai, phai)

n_b13 = NutBai13(3)
n_b13.tiep_theo = NutBai13(1)
n_b13.tiep_theo.tiep_theo = NutBai13(2)
kq_sap_xep = merge_sort_linked_list(n_b13)
chuoi_b13 = []
while kq_sap_xep:
    chuoi_b13.append(str(kq_sap_xep.du_lieu))
    kq_sap_xep = kq_sap_xep.tiep_theo
print("Bai 13: ", "->".join(chuoi_b13))


# --- BÀI 14
class NutBai14:
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.tiep_theo = None

def cong_hai_so_linked_list(l1, l2):
    nut_gia = NutBai14(0)
    hien_tai = nut_gia
    nho = 0
    while l1 or l2 or nho:
        tong = nho
        if l1:
            tong += l1.du_lieu
            l1 = l1.tiep_theo
        if l2:
            tong += l2.du_lieu
            l2 = l2.tiep_theo
        nho = tong // 10
        hien_tai.tiep_theo = NutBai14(tong % 10)
        hien_tai = hien_tai.tiep_theo
    return nut_gia.tiep_theo

ds1 = NutBai14(2)
ds1.tiep_theo = NutBai14(4)
ds1.tiep_theo.tiep_theo = NutBai14(3)

ds2 = NutBai14(5)
ds2.tiep_theo = NutBai14(6)
ds2.tiep_theo.tiep_theo = NutBai14(4)

kq_cong = cong_hai_so_linked_list(ds1, ds2)
chuoi_b14 = []
while kq_cong:
    chuoi_b14.append(str(kq_cong.du_lieu))
    kq_cong = kq_cong.tiep_theo
print("Bai 14: ", "->".join(chuoi_b14))


# --- BÀI 15
class NutCache:
    def __init__(self, khoa, gia_tri):
        self.khoa = khoa
        self.gia_tri = gia_tri
        self.truoc = None
        self.tiep_theo = None

class LRUCache:
    def __init__(self, dung_luong):
        self.dung_luong = dung_luong
        self.ban_do = {}
        self.dau = NutCache(0, 0)
        self.cuoi = NutCache(0, 0)
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
            self._them_vao_dau(nut)
            return nut.gia_tri
        return -1

    def put(self, khoa, gia_tri):
        if khoa in self.ban_do:
            self._xoa_nut(self.ban_do[khoa])
        nut_moi = NutCache(khoa, gia_tri)
        self._them_vao_dau(nut_moi)
        self.ban_do[khoa] = nut_moi
        if len(self.ban_do) > self.dung_luong:
            nut_duoi = self.cuoi.truoc
            self._xoa_nut(nut_duoi)
            del self.ban_do[nut_duoi.khoa]

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
v1 = cache.get(1)
cache.put(3, 3)
v2 = cache.get(2)
print("Bai 15: ", f"Lay khoa 1: {v1} | Lay khoa 2: {v2}")
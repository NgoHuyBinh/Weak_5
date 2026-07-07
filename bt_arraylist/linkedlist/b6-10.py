class Nut:
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.tiep_theo = None


# --- BÀI 6
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

ds_bai_6 = DanhSachDaoNguoc()
ds_bai_6.pushBack(1)
ds_bai_6.pushBack(2)
ds_bai_6.pushBack(3)
ds_bai_6.dao_nguoc_lap()
kq_lap = ds_bai_6.in_toan_bo()
ds_bai_6.dao_nguoc_de_quy()
kq_de_quy = ds_bai_6.in_toan_bo()
print("Bai 6: ", f"Lap: {kq_lap} | De quy: {kq_de_quy}")


# --- BÀI 7
class DanhSachNutGiua:
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

    def tim_nut_giua(self):
        chong = self.dau
        nhanh = self.dau
        while nhanh and nhanh.tiep_theo:
            chong = chong.tiep_theo
            nhanh = nhanh.tiep_theo.tiep_theo
        return chong.du_lieu if chong else None

ds_bai_7 = DanhSachNutGiua()
for v in [1, 2, 3, 4, 5]:
    ds_bai_7.pushBack(v)
print("Bai 7: ", ds_bai_7.tim_nut_giua())


# --- BÀI 8
class DanhSachChuTrinh:
    def __init__(self):
        self.dau = None

    def phat_hien_chu_trinh(self):
        rua = self.dau
        tho = self.dau
        while tho and tho.tiep_theo:
            rua = rua.tiep_theo
            tho = tho.tiep_theo.tiep_theo
            if rua == tho:
                return True
        return False

ds_bai_8 = DanhSachChuTrinh()
n1 = Nut(1)
n2 = Nut(2)
n3 = Nut(3)
ds_bai_8.dau = n1
n1.tiep_theo = n2
n2.tiep_theo = n3
n3.tiep_theo = n2
print("Bai 8: ", ds_bai_8.phat_hien_chu_trinh())


# --- BÀI 9
def tron_hai_danh_sach_lk(l1, l2):
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
        
    if l1:
        hien_tai.tiep_theo = l1
    if l2:
        hien_tai.tiep_theo = l2
        
    return nut_gia.tiep_theo

ds1_n1 = Nut(1)
ds1_n2 = Nut(3)
ds1_n3 = Nut(5)
ds1_n1.tiep_theo = ds1_n2
ds1_n2.tiep_theo = ds1_n3

ds2_n1 = Nut(2)
ds2_n2 = Nut(4)
ds2_n1.tiep_theo = ds2_n2

kq_dau = tron_hai_danh_sach_lk(ds1_n1, ds2_n1)
chuoi_kq_9 = []
while kq_dau:
    chuoi_kq_9.append(str(kq_dau.du_lieu))
    kq_dau = kq_dau.tiep_theo
chuoi_kq_9.append("null")
print("Bai 9: ", "->".join(chuoi_kq_9))


# --- BÀI 10
class DanhSachXoaKTuCuoi:
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

    def xoa_nut_k_tu_cuoi(self, k):
        nut_gia = Nut(0)
        nut_gia.tiep_theo = self.dau
        nhanh = nut_gia
        chong = nut_gia
        
        for _ in range(k + 1):
            nhanh = nhanh.tiep_theo
            
        while nhanh:
            nhanh = nhanh.tiep_theo
            chong = chong.tiep_theo
            
        chong.tiep_theo = chong.tiep_theo.tiep_theo
        self.dau = nut_gia.tiep_theo

    def in_toan_bo(self):
        chuoi_kq = []
        hien_tai = self.dau
        while hien_tai:
            chuoi_kq.append(str(hien_tai.du_lieu))
            hien_tai = hien_tai.tiep_theo
        chuoi_kq.append("null")
        return "->".join(chuoi_kq)

ds_bai_10 = DanhSachXoaKTuCuoi()
for v in [1, 2, 3, 4, 5]:
    ds_bai_10.pushBack(v)
ds_bai_10.xoa_nut_k_tu_cuoi(2)
print("Bai 10: ", ds_bai_10.in_toan_bo())
#BAI 1
class NganXepMang:
    def __init__(self):
        self.danh_sach = []
    def day_vao(self, gia_tri):
        self.danh_sach.append(gia_tri)
    def lay_ra(self):
        if not self.kiem_tra_rong():
            return self.danh_sach.pop()
        return None
    def dinh_ngan_xep(self):
        if not self.kiem_tra_rong():
            return self.danh_sach[-1]
        return None
    def kiem_tra_rong(self):
        return len(self.danh_sach) == 0

nx_bai_1 = NganXepMang()
nx_bai_1.day_vao(1)
nx_bai_1.day_vao(2)
nx_bai_1.day_vao(3)
kq_bai_1 = nx_bai_1.lay_ra()
print("Bai 1: ", kq_bai_1)

#BAI 2
def dao_nguoc_chuoi(chuoi_goc):
    ngan_xep = []
    for ky_tu in chuoi_goc:
        ngan_xep.append(ky_tu)
    chuoi_dao_nguoc = ""
    while len(ngan_xep) > 0:
        chuoi_dao_nguoc += ngan_xep.pop()
    return chuoi_dao_nguoc

kq_bai_2 = dao_nguoc_chuoi("abc")
print("Bai 2: ", kq_bai_2)

#BAI 3
def mo_phong_thao_tac(day_lenh):
    ngan_xep = []
    ket_qua_pop = []
    for lenh in day_lenh:
        if lenh[0] == "push":
            ngan_xep.append(lenh[1])
        elif lenh[0] == "pop":
            if len(ngan_xep) > 0:
                ket_qua_pop.append(ngan_xep.pop())
    return ket_qua_pop, ngan_xep

day_lenh_mau = [("push", 5), ("push", 7), ("pop")]
kq_pop, trang_thai_cuoi = mo_phong_thao_tac(day_lenh_mau)
print("Bai 3: ", f"Gia tri pop: {kq_pop}, Trang thai cuoi: {trang_thai_cuoi}")

#BAI 4
class NganXepCoHan:
    def __init__(self, dung_luong_toi_da):
        self.danh_sach = []
        self.dung_luong = dung_luong_toi_da
    def day_vao(self, gia_tri):
        if len(self.danh_sach) >= self.dung_luong:
            return "báo lỗi overflow"
        self.danh_sach.append(gia_tri)
        return "thanh_cong"
    def lay_ra(self):
        if len(self.danh_sach) == 0:
            return "báo lỗi underflow"
        return self.danh_sach.pop()

nx_bai_4 = NganXepCoHan(2)
nx_bai_4.day_vao(1)
nx_bai_4.day_vao(2)
loi_overflow = nx_bai_4.day_vao(3)
nx_bai_4.lay_ra()
nx_bai_4.lay_ra()
loi_underflow = nx_bai_4.lay_ra()
print("Bai 4: ", f"{loi_overflow} | {loi_underflow}")

#BAI 5
def duyet_va_dem_phan_tu(ngan_xep_goc):
    ngan_xep_phu = []
    chuoi_phan_tu = []
    so_luong = 0
    while len(ngan_xep_goc) > 0:
        gia_tri = ngan_xep_goc.pop()
        chuoi_phan_tu.append(str(gia_tri))
        so_luong += 1
        ngan_xep_phu.append(gia_tri)
    while len(ngan_xep_phu) > 0:
        ngan_xep_goc.append(ngan_xep_phu.pop())
    return so_luong, ", ".join(chuoi_phan_tu), ngan_xep_goc

stack_goc = [1, 2, 3]
dem, cac_phan_tu, stack_sau_khi_giu = duyet_va_dem_phan_tu(stack_goc)
print("Bai 5: ", f"So luong: {dem}, Thu tu LIFO: {cac_phan_tu}, Stack goc giu nguyen: {stack_sau_khi_giu}")
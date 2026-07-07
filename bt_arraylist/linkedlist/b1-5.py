# --- KHỞI TẠO NOTE ĐỂ LIÊN KẾT
class Nut:
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.tiep_theo = None


# --- BÀI 1
class DanhSachLienKetDon:
    def __init__(self):
        self.dau = None

    def pushFront(self, gia_tri):
        nut_moi = Nut(gia_tri)
        nut_moi.tiep_theo = self.dau
        self.dau = nut_moi

    def pushBack(self, gia_tri):
        nut_moi = Nut(gia_tri)
        if not self.dau:
            self.dau = nut_moi
            return
        hien_tai = self.dau
        while hien_tai.tiep_theo:
            hien_tai = hien_tai.tiep_theo
        hien_tai.tiep_theo = nut_moi

    def in_toan_bo(self):
        chuoi_kq = []
        hien_tai = self.dau
        while hien_tai:
            chuoi_kq.append(str(hien_tai.du_lieu))
            hien_tai = hien_tai.tiep_theo
        chuoi_kq.append("null")
        return "->".join(chuoi_kq)

ds_bai_1 = DanhSachLienKetDon()
ds_bai_1.pushFront(2)
ds_bai_1.pushBack(5)
print("Bai 1: ", ds_bai_1.in_toan_bo())


# --- BÀI 2
class DanhSachDuyet(DanhSachLienKetDon):
    def tinh_do_dai(self):
        dem = 0
        hien_tai = self.dau
        while hien_tai:
            dem += 1
            hien_tai = hien_tai.tiep_theo
        return dem

ds_bai_2 = DanhSachDuyet()
ds_bai_2.pushBack(1)
ds_bai_2.pushBack(2)
ds_bai_2.pushBack(3)
print("Bai 2: ", ds_bai_2.tinh_do_dai())


# --- BÀI 3
class DanhSachTimKiem(DanhSachLienKetDon):
    def tim_kiem(self, gia_tri_tim):
        chi_so = 0
        hien_tai = self.dau
        while hien_tai:
            if hien_tai.du_lieu == gia_tri_tim:
                return chi_so
            chi_so += 1
            hien_tai = hien_tai.tiep_theo
        return -1

ds_bai_3 = DanhSachTimKiem()
ds_bai_3.pushBack(1)
ds_bai_3.pushBack(2)
ds_bai_3.pushBack(3)
print("Bai 3: ", ds_bai_3.tim_kiem(2))


# --- BÀI 4
class DanhSachChenSau(DanhSachLienKetDon):
    def chen_sau_gia_tri(self, gia_tri_muc_tieu, gia_tri_moi):
        hien_tai = self.dau
        while hien_tai:
            if hien_tai.du_lieu == gia_tri_muc_tieu:
                nut_moi = Nut(gia_tri_moi)
                nut_moi.tiep_theo = hien_tai.tiep_theo
                hien_tai.tiep_theo = nut_moi
                return True
            hien_tai = hien_tai.tiep_theo
        return False

ds_bai_4 = DanhSachChenSau()
ds_bai_4.pushBack(1)
ds_bai_4.pushBack(3)
ds_bai_4.chen_sau_gia_tri(1, 2)
print("Bai 4: ", ds_bai_4.in_toan_bo())


# --- BÀI 5
class DanhSachXoaNut(DanhSachLienKetDon):
    def xoa_nut_dau_tien(self, x):
        if not self.dau:
            return
        
        if self.dau.du_lieu == x:
            self.dau = self.dau.tiep_theo
            return

        hien_tai = self.dau
        while hien_tai.tiep_theo:
            if hien_tai.tiep_theo.du_lieu == x:
                hien_tai.tiep_theo = hien_tai.tiep_theo.tiep_theo
                return
            hien_tai = hien_tai.tiep_theo

ds_bai_5 = DanhSachXoaNut()
ds_bai_5.pushBack(1)
ds_bai_5.pushBack(2)
ds_bai_5.pushBack(3)
ds_bai_5.pushBack(2)
ds_bai_5.xoa_nut_dau_tien(2)
print("Bai 5: ", ds_bai_5.in_toan_bo())
# --- BÀI 6
class ArrayListResizing:
    def __init__(self, dung_luong_ban_dau=4):
        self.mang = [None] * dung_luong_ban_dau
        self.so_luong = 0
        self.dung_luong = dung_luong_ban_dau

    def add(self, gia_tri):
        if self.so_luong == self.dung_luong:
            self.dung_luong *= 2
            mang_moi = [None] * self.dung_luong
            for i in range(self.so_luong):
                mang_moi[i] = self.mang[i]
            self.mang = mang_moi
            
        self.mang[self.so_luong] = gia_tri
        self.so_luong += 1

ds_bai_6 = ArrayListResizing(4)
for v in [1, 2, 3, 4, 5]:
    ds_bai_6.add(v)
print("Bai 6: ", f"Dung luong moi: {ds_bai_6.dung_luong}, Mang: {ds_bai_6.mang[:ds_bai_6.so_luong]}")


# --- BÀI 7
def chung_minh_amortized(n):
    tong_chi_phi = 0
    dung_luong = 1
    so_luong = 0
    
    for i in range(n):
        if so_luong == dung_luong:
            dung_luong *= 2
            tong_chi_phi += so_luong
            
        tong_chi_phi += 1
        so_luong += 1
        
    chi_phi_trung_binh = tong_chi_phi / n
    return chi_phi_trung_binh

kq_bai_7 = chung_minh_amortized(1000)
print("Bai 7: ", f"Chi phi trung binh moi phat append: {kq_bai_7}")


# --- BÀI 8
class ArrayListRemoveIf:
    def __init__(self):
        self.mang = [1, 2, 3, 4]
        self.so_luong = 4

    def removeIf(self):
        con_tro_ghi = 0
        for con_tro_doc in range(self.so_luong):
            if self.mang[con_tro_doc] % 2 != 0:
                self.mang[con_tro_ghi] = self.mang[con_tro_doc]
                con_tro_ghi += 1
        self.so_luong = con_tro_ghi

ds_bai_8 = ArrayListRemoveIf()
ds_bai_8.removeIf()
print("Bai 8: ", ds_bai_8.mang[:ds_bai_8.so_luong])


# --- BÀI 9
class ArrayListReverse:
    def __init__(self):
        self.mang = [1, 2, 3, 4]

    def reverse(self):
        trai = 0
        phai = len(self.mang) - 1
        while trai < phai:
            self.mang[trai], self.mang[phai] = self.mang[phai], self.mang[trai]
            trai += 1
            phai -= 1

ds_bai_9 = ArrayListReverse()
ds_bai_9.reverse()
print("Bai 9: ", ds_bai_9.mang)


# --- BÀI 10
def tron_hai_danh_sach(ds1, ds2):
    ket_qua = []
    i = 0
    j = 0
    
    while i < len(ds1) and j < len(ds2):
        if ds1[i] <= ds2[j]:
            ket_qua.append(ds1[i])
            i += 1
        else:
            ket_qua.append(ds2[j])
            j += 1
            
    while i < len(ds1):
        ket_qua.append(ds1[i])
        i += 1
        
    while j < len(ds2):
        ket_qua.append(ds2[j])
        j += 1
        
    return ket_qua

mang_1 = [1, 3, 5]
mang_2 = [2, 4]
kq_bai_10 = tron_hai_danh_sach(mang_1, mang_2)
print("Bai 10: ", kq_bai_10)
# --- BÀI 11
class ArrayListXoay:
    def __init__(self):
        self.mang = [1, 2, 3, 4, 5]

    def dao_doan(self, trai, phai):
        while trai < phai:
            self.mang[trai], self.mang[phai] = self.mang[phai], self.mang[trai]
            trai += 1
            phai -= 1

    def xoay_phai(self, k):
        n = len(self.mang)
        k = k % n
        if k == 0:
            return
        self.dao_doan(0, n - 1)
        self.dao_doan(0, k - 1)
        self.dao_doan(k, n - 1)

ds_bai_11 = ArrayListXoay()
ds_bai_11.xoay_phai(2)
print("Bai 11: ", ds_bai_11.mang)


# --- BÀI 12
class ArrayListXoaTrung:
    def __init__(self):
        self.mang = [3, 1, 3, 2, 1]

    def loai_bo_trung_lap(self):
        tap_bam = set()
        mang_moi = []
        for gia_tri in self.mang:
            if gia_tri not in tap_bam:
                tap_bam.add(gia_tri)
                mang_moi.append(gia_tri)
        self.mang = mang_moi

ds_bai_12 = ArrayListXoaTrung()
ds_bai_12.loai_bo_trung_lap()
print("Bai 12: ", ds_bai_12.mang)


# --- BÀI 13
def tron_cac_khoang(danh_sach_khoang):
    if not danh_sach_khoang:
        return []
    
    danh_sach_khoang.sort(key=lambda x: x[0])
    ket_qua = [danh_sach_khoang[0]]
    
    for i in range(1, len(danh_sach_khoang)):
        khoang_hien_tai = danh_sach_khoang[i]
        khoang_cuoi_cung = ket_qua[-1]
        
        if khoang_hien_tai[0] <= khoang_cuoi_cung[1]:
            khoang_cuoi_cung[1] = max(khoang_cuoi_cung[1], khoang_hien_tai[1])
        else:
            ket_qua.append(khoang_hien_tai)
            
    return ket_qua

mang_khoang = [[1, 3], [2, 6], [8, 10]]
kq_bai_13 = tron_cac_khoang(mang_khoang)
print("Bai 13: ", kq_bai_13)


# --- BÀI 14
class MangDongHaiChieu:
    def __init__(self):
        self.ma_tran = []

    def them_hang(self, hang_moi):
        self.ma_tran.append(hang_moi)

    def set(self, i, j, gia_tri):
        if i < len(self.ma_tran) and j < len(self.ma_tran[i]):
            self.ma_tran[i][j] = gia_tri

    def get(self, i, j):
        if i < len(self.ma_tran) and j < len(self.ma_tran[i]):
            return self.ma_tran[i][j]
        return None

mt = MangDongHaiChieu()
mt.them_hang([1, 2, 3])
mt.them_hang([4, 5, 6])
mt.set(0, 1, 9)
kq_bai_14 = mt.get(0, 1)
print("Bai 14: ", f"Gia tri tai (0,1): {kq_bai_14}, Ma tran: {mt.ma_tran}")


# --- BÀI 15
class ArrayListWithIterator:
    def __init__(self):
        self.mang = [10, 20, 30]
        self.modCount = 0

    def add(self, gia_tri):
        self.mang.append(gia_tri)
        self.modCount += 1

    def remove_at(self, chi_so):
        self.mang.pop(chi_so)
        self.modCount += 1

    def __iter__(self):
        return ArrayListIterator(self)

class ArrayListIterator:
    def __init__(self, list_obj):
        self.list_obj = list_obj
        self.chi_so_hien_tai = 0
        self.expectedModCount = list_obj.modCount

    def __next__(self):
        if self.list_obj.modCount != self.expectedModCount:
            raise RuntimeError("loi ")
        if self.chi_so_hien_tai >= len(self.list_obj.mang):
            raise StopIteration
        gia_tri = self.list_obj.mang[self.chi_so_hien_tai]
        self.chi_so_hien_tai += 1
        return gia_tri

ds = ArrayListWithIterator()
try:
    for phan_tu in ds:
        ds.add(40)
except RuntimeError as e:
    print("Bai 15: ", str(e))
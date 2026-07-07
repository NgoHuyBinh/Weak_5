# --- CÂU 31
class DynamicArrayList:
    def __init__(self, dung_luong_ban_dau=4):
        self.mang = [None] * dung_luong_ban_dau
        self.so_luong = 0
        self.dung_luong = dung_luong_ban_dau

    def append(self, gia_tri):
        if self.so_luong == self.dung_luong:
            self.dung_luong *= 2
            mang_moi = [None] * self.dung_luong
            for i in range(self.so_luong):
                mang_moi[i] = self.mang[i]
            self.mang = mang_moi
            
        self.mang[self.so_luong] = gia_tri
        self.so_luong += 1

ds_31 = DynamicArrayList(2)
ds_31.append(10)
ds_31.append(20)
ds_31.append(30)  # Kích hoạt tạo mảng mới dung lượng 4
print("Cau 31: ", f"Dung luong: {ds_31.dung_luong}, Mang: {ds_31.mang[:ds_31.so_luong]}")


# --- CÂU 32
def remove_if_tai_cho(mang, dieu_kien_xoa):
    # Kỹ thuật hai con trỏ đọc và ghi để đạt O(n) thời gian, O(1) bộ nhớ
    con_tro_ghi = 0
    for con_tro_doc in range(len(mang)):
        if not dieu_kien_xoa(mang[con_tro_doc]):
            mang[con_tro_ghi] = mang[con_tro_doc]
            con_tro_ghi += 1
            
    del mang[con_tro_ghi:]
    return mang

mang_32 = [1, 2, 3, 4]
# Ví dụ: Xóa các số chẵn
print("Cau 32: ", remove_if_tai_cho(mang_32, lambda x: x % 2 == 0))


# --- CÂU 33
def xoay_mang_k_vi_tri(mang, k):
    n = len(mang)
    if n == 0: return mang
    k = k % n
    if k == 0: return mang

    # Kỹ thuật đảo ba lần để đạt O(n) tại chỗ
    def dao_doan(trai, phai):
        while trai < phai:
            mang[trai], mang[phai] = mang[phai], mang[trai]
            trai += 1
            phai -= 1

    dao_doan(0, n - 1)      # Bước 1: Đảo ngược toàn bộ mảng
    dao_doan(0, k - 1)      # Bước 2: Đảo ngược k phần tử đầu tiên
    dao_doan(k, n - 1)      # Bước 3: Đảo ngược các phần tử còn lại
    return mang

mang_33 = [1, 2, 3, 4, 5]
print("Cau 33: ", xoay_mang_k_vi_tri(mang_33, 2))


# --- CÂU 34
def loai_bo_trung_lap_hash(mang):
    tap_bam = set()
    ket_qua = []
    for gia_tri in mang:
        if gia_tri not in tap_bam:
            tap_bam.add(gia_tri)
            ket_qua.append(gia_tri)
    return ket_qua

mang_34 = [3, 1, 3, 2, 1]
print("Cau 34: ", loai_bo_trung_lap_hash(mang_34))


# --- CÂU 35
def merge_intervals(cac_khoang):
    if not cac_khoang:
        return []
    
    # Sắp xếp các khoảng dựa trên điểm bắt đầu (start)
    cac_khoang.sort(key=lambda x: x[0])
    ket_qua = [cac_khoang[0]]
    
    # Quét một lượt các khoảng còn lại
    for i in range(1, len(cac_khoang)):
        khoang_hien_tai = cac_khoang[i]
        khoang_cuoi_cung = ket_qua[-1]
        
        # Nếu điểm bắt đầu của khoảng hiện tại nhỏ hơn hoặc bằng điểm kết thúc khoảng trước -> giao nhau
        if khoang_hien_tai[0] <= khoang_cuoi_cung[1]:
            khoang_cuoi_cung[1] = max(khoang_cuoi_cung[1], khoang_hien_tai[1])
        else:
            ket_qua.append(khoang_hien_tai)
            
    return ket_qua

mang_khoang_35 = [[1, 3], [2, 6], [8, 10]]
print("Cau 35: ", merge_intervals(mang_khoang_35))
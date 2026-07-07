# --- BÀI 6: SO SÁNH CHAINING VS OPEN ADDRESSING
    # Chaining: Tốn bộ nhớ cho con trỏ, hiệu năng tốt khi load factor > 1, xóa phần tử dễ dàng bằng cách hủy nút trong danh sách liên kết.
    # Open Addressing: Tiết kiệm bộ nhớ (không dùng con trỏ), hiệu năng giảm mạnh khi load factor cao (clustering), xóa phần tử cần dùng cờ đặc biệt (như DELETED).

# --- BÀI 7
class BangBamRehash:
    def __init__(self, kich_thuoc_ban_dau=4):
        self.kich_thuoc = kich_thuoc_ban_dau
        self.cac_khoa = [None] * self.kich_thuoc
        self.cac_gia_tri = [None] * self.kich_thuoc
        self.so_luong = 0

    def _ham_bam(self, khoa, kich_thuoc_hien_tai):
        return hash(khoa) % kich_thuoc_hien_tai

    def _rehash(self):
        kich_thuoc_moi = self.kich_thuoc * 2
        mang_khoa_cu = self.cac_khoa
        mang_gia_tri_cu = self.cac_gia_tri

        self.kich_thuoc = kich_thuoc_moi
        self.cac_khoa = [None] * kich_thuoc_moi
        self.cac_gia_tri = [None] * kich_thuoc_moi
        self.so_luong = 0

        for i in range(len(mang_khoa_cu)):
            if mang_khoa_cu[i] is not None and mang_khoa_cu[i] != "DELETED":
                self.put(mang_khoa_cu[i], mang_gia_tri_cu[i])

    def put(self, khoa, gia_tri):
        if self.so_luong / self.kich_thuoc > 0.75:
            self._rehash()

        idx = self._ham_bam(khoa, self.kich_thuoc)
        while self.cac_khoa[idx] is not None and self.cac_khoa[idx] != "DELETED":
            if self.cac_khoa[idx] == khoa:
                self.cac_gia_tri[idx] = gia_tri
                return
            idx = (idx + 1) % self.kich_thuoc

        if self.cac_khoa[idx] is None or self.cac_khoa[idx] == "DELETED":
            self.so_luong += 1
        self.cac_khoa[idx] = khoa
        self.cac_gia_tri[idx] = gia_tri

    def get(self, khoa):
        idx = self._ham_bam(khoa, self.kich_thuoc)
        goc = idx
        while self.cac_khoa[idx] is not None:
            if self.cac_khoa[idx] == khoa:
                return self.cac_gia_tri[idx]
            idx = (idx + 1) % self.kich_thuoc
            if idx == goc:
                break
        return None

bb_7 = BangBamRehash(4)
for v in range(5):
    bb_7.put(f'khoa_{v}', v)
print("Bai 7: ", f"Kich thuoc sau rehash: {bb_7.kich_thuoc}, Lay gia tri: {bb_7.get('khoa_4')}")


# --- BÀI 8
class BangBamDoMởRộng:
    def __init__(self, kich_thuoc=11):
        self.kich_thuoc = kich_thuoc
        self.cac_khoa = [None] * kich_thuoc
        self.cac_gia_tri = [None] * kich_thuoc

    def _ham_bam_1(self, khoa):
        return hash(khoa) % self.kich_thuoc

    def _ham_bam_2(self, khoa):
        return 7 - (hash(khoa) % 7)

    def put_quadratic(self, khoa, gia_tri):
        idx = self._ham_bam_1(khoa)
        i = 0
        while self.cac_khoa[(idx + i * i) % self.kich_thuoc] is not None:
            if self.cac_khoa[(idx + i * i) % self.kich_thuoc] == khoa:
                self.cac_gia_tri[(idx + i * i) % self.kich_thuoc] = gia_tri
                return
            i += 1
        self.cac_khoa[(idx + i * i) % self.kich_thuoc] = khoa
        self.cac_gia_tri[(idx + i * i) % self.kich_thuoc] = gia_tri

    def put_double_hash(self, khoa, gia_tri):
        h1 = self._ham_bam_1(khoa)
        h2 = self._ham_bam_2(khoa)
        i = 0
        while self.cac_khoa[(h1 + i * h2) % self.kich_thuoc] is not None:
            if self.cac_khoa[(h1 + i * h2) % self.kich_thuoc] == khoa:
                self.cac_gia_tri[(h1 + i * h2) % self.kich_thuoc] = gia_tri
                return
            i += 1
        self.cac_khoa[(h1 + i * h2) % self.kich_thuoc] = khoa
        self.cac_gia_tri[(h1 + i * h2) % self.kich_thuoc] = gia_tri

bb_8 = BangBamDoMởRộng()
bb_8.put_quadratic('a', 10)
bb_8.put_double_hash('b', 20)
print("Bai 8: ", "Da thuc hien chen phan tu bang Quadratic va Double Hashing")


# --- BÀI 9
def two_sum_hash(mang_a, target):
    bang_bam = {}
    for i in range(len(mang_a)):
        phan_bu = target - mang_a[i]
        if phan_bu in bang_bam:
            return (bang_bam[phan_bu], i)
        bang_bam[mang_a[i]] = i
    return None

mang_9 = [2, 7, 11]
dich = 9
print("Bai 9: ", two_sum_hash(mang_9, dich))


# --- BÀI 10
def phan_tu_khong_lap_dau_tien(chuoi_ky_tu):
    bang_dem = {}
    for ky_tu in chuoi_ky_tu:
        if ky_tu in bang_dem:
            bang_dem[ky_tu] += 1
        else:
            bang_dem[ky_tu] = 1

    for ky_tu in chuoi_ky_tu:
        if bang_dem[ky_tu] == 1:
            return ky_tu
    return None

chuoi_b10 = 'leetcode'
print("Bai 10: ", phan_tu_khong_lap_dau_tien(chuoi_b10))
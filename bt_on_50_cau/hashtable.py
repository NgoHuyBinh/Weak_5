# --- CÂU 42
class NutBam:
    def __init__(self, khoa, gia_tri):
        self.khoa = khoa
        self.gia_tri = gia_tri
        self.tiep_theo = None

class BangBamChaining:
    def __init__(self, kich_thuoc=10):
        self.kich_thuoc = kich_thuoc
        self.cac_o = [None] * kich_thuoc

    def _ham_bam(self, khoa):
        return hash(khoa) % self.kich_thuoc

    def put(self, khoa, gia_tri):
        idx = self._ham_bam(khoa)
        if not self.cac_o[idx]:
            self.cac_o[idx] = NutBam(khoa, gia_tri)
            return
        hien_tai = self.cac_o[idx]
        while True:
            if hien_tai.khoa == khoa:
                hien_tai.gia_tri = gia_tri
                return
            if not hien_tai.tiep_theo:
                break
            hien_tai = hien_tai.tiep_theo
        hien_tai.tiep_theo = NutBam(khoa, gia_tri)

    def get(self, khoa):
        idx = self._ham_bam(khoa)
        hien_tai = self.cac_o[idx]
        while hien_tai:
            if hien_tai.khoa == khoa:
                return hien_tai.gia_tri
            hien_tai = hien_tai.tiep_theo
        return None

    def remove(self, khoa):
        idx = self._ham_bam(khoa)
        hien_tai = self.cac_o[idx]
        truoc = None
        while hien_tai:
            if hien_tai.khoa == khoa:
                if truoc:
                    truoc.tiep_theo = hien_tai.tiep_theo
                else:
                    self.cac_o[idx] = hien_tai.tiep_theo
                return True
            truoc = hien_tai
            hien_tai = hien_tai.tiep_theo
        return False

bb_42 = BangBamChaining()
bb_42.put('a', 1)
print("Cau 42: ", bb_42.get('a'))


# --- CÂU 43
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

bb_43 = BangBamRehash(4)
for v in range(5):
    bb_43.put(f'k_{v}', v)
print("Cau 43 (Kich thuoc sau khi gap doi): ", bb_43.kich_thuoc)


# --- CÂU 44
def two_sum_hash(mang_a, target):
    bang_bam = {}
    for i in range(len(mang_a)):
        phan_bu = target - mang_a[i]
        if phan_bu in bang_bam:
            return (bang_bam[phan_bu], i)
        bang_bam[mang_a[i]] = i
    return None

print("Cau 44: ", two_sum_hash([2, 7, 11], 9))


# --- CÂU 45
def dem_doan_con_tong_k(mang_a, k):
    bang_bam = {0: 1}  # Giá trị mặc định cho tổng tiền tố bằng đúng k
    tong_tien_to = 0
    so_luong_doan = 0
    
    for phan_tu in mang_a:
        tong_tien_to += phan_tu
        phan_bu = tong_tien_to - k
        
        if phan_bu in bang_bam:
            so_luong_doan += bang_bam[phan_bu]
            
        if tong_tien_to in bang_bam:
            bang_bam[tong_tien_to] += 1
        else:
            bang_bam[tong_tien_to] = 1
            
    return so_luong_doan

print("Cau 45: ", dem_doan_con_tong_k([1, 1, 1], 2))


# --- CÂU 46
def day_lien_tiep_dai_nhat(mang_a):
    tap_hop_bam = set(mang_a)
    chieu_dai_max = 0
    
    for phan_tu in mang_a:
        if phan_tu - 1 not in tap_hop_bam:
            so_hien_tai = phan_tu
            chieu_dai_hien_tai = 1
            
            while so_hien_tai + 1 in tap_hop_bam:
                so_hien_tai += 1
                chieu_dai_hien_tai += 1
                
            chieu_dai_max = max(chieu_dai_max, chieu_dai_hien_tai)
            
    return chieu_dai_max

print("Cau 46: ", day_lien_tiep_dai_nhat([100, 4, 200, 1, 3, 2]))
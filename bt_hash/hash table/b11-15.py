# --- BÀI 11
class HashSetCoBan:
    def __init__(self, kich_thuoc=10):
        self.kich_thuoc = kich_thuoc
        self.cac_o = [[] for _ in range(kich_thuoc)]

    def _ham_bam(self, khoa):
        return hash(khoa) % self.kich_thuoc

    def add(self, khoa):
        idx = self._ham_bam(khoa)
        if khoa not in self.cac_o[idx]:
            self.cac_o[idx].append(khoa)

    def contains(self, khoa):
        idx = self._ham_bam(khoa)
        return khoa in self.cac_o[idx]

    def remove(self, khoa):
        idx = self._ham_bam(khoa)
        if khoa in self.cac_o[idx]:
            self.cac_o[idx].remove(khoa)
            return True
        return False

hs_11 = HashSetCoBan()
hs_11.add(1)
hs_11.add(1)
hs_11.add(2)
print("Bai 11: ", f"Chua phan tu 1: {hs_11.contains(1)}, Chua phan tu 3: {hs_11.contains(3)}")


# --- BÀI 12
def dem_doan_con_tong_k(mang_a, k):
    bang_bam = {0: 1}
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

mang_12 = [1, 1, 1]
k_12 = 2
print("Bai 12: ", dem_doan_con_tong_k(mang_12, k_12))


# --- BÀI 13
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

mang_13 = [100, 4, 200, 1, 3, 2]
print("Bai 13: ", day_lien_tiep_dai_nhat(mang_13))


# --- BÀI 14
class BangBamXoaLuoi:
    def __init__(self, kich_thuoc=10):
        self.kich_thuoc = kich_thuoc
        self.cac_khoa = [None] * kich_thuoc
        self.cac_gia_tri = [None] * kich_thuoc
        self.so_luong_del = 0

    def _ham_bam(self, khoa):
        return hash(khoa) % self.kich_thuoc

    def put(self, khoa, gia_tri):
        idx = self._ham_bam(khoa)
        vi_tri_del_dau_tien = None
        goc = idx
        
        while self.cac_khoa[idx] is not None:
            if self.cac_khoa[idx] == "DELETED":
                if vi_tri_del_dau_tien is None:
                    vi_tri_del_dau_tien = idx
            elif self.cac_khoa[idx] == khoa:
                self.cac_gia_tri[idx] = gia_tri
                return
            idx = (idx + 1) % self.kich_thuoc
            if idx == goc:
                break
                
        vi_tri_chen = vi_tri_del_dau_tien if vi_tri_del_dau_tien is not None else idx
        if self.cac_khoa[vi_tri_chen] == "DELETED":
            self.so_luong_del -= 1
        self.cac_khoa[vi_tri_chen] = khoa
        self.cac_gia_tri[vi_tri_chen] = gia_tri

    def remove(self, khoa):
        idx = self._ham_bam(khoa)
        goc = idx
        while self.cac_khoa[idx] is not None:
            if self.cac_khoa[idx] == khoa:
                self.cac_khoa[idx] = "DELETED"
                self.cac_gia_tri[idx] = None
                self.so_luong_del += 1
                return True
            idx = (idx + 1) % self.kich_thuoc
            if idx == goc:
                break
        return False

bb_14 = BangBamXoaLuoi()
bb_14.put('a', 10)
bb_14.remove('a')
print("Bai 14: ", f"Trang thai o cua khoa 'a': {bb_14.cac_khoa[bb_14._ham_bam('a')]}")


# --- BÀI 15
import bisect

class BamNhatQuan:
    def __init__(self, so_nut_ao=3):
        self.so_nut_ao = so_nut_ao
        self.vong_bam = []
        self.ban_do_nut = {}

    def _hash(self, chuoi_khoa):
        return hash(chuoi_khoa) & 0xFFFFFFFF

    def them_may_chu(self, may_chu):
        for i in range(self.so_nut_ao):
            khoa_nut_ao = self._hash(f"{may_chu}-ao-{i}")
            bisect.insort(self.vong_bam, khoa_nut_ao)
            self.ban_do_nut[khoa_nut_ao] = may_chu

    def bot_may_chu(self, may_chu):
        for i in range(self.so_nut_ao):
            khoa_nut_ao = self._hash(f"{may_chu}-ao-{i}")
            idx = bisect.bisect_left(self.vong_bam, khoa_nut_ao)
            if idx < len(self.vong_bam) and self.vong_bam[idx] == khoa_nut_ao:
                self.vong_bam.pop(idx)
                del self.ban_do_nut[khoa_nut_ao]

    def lay_may_chu(self, khoa_du_lieu):
        if not self.vong_bam:
            return None
        gia_tri_bam = self._hash(khoa_du_lieu)
        idx = bisect.bisect_right(self.vong_bam, gia_tri_bam)
        if idx == len(self.vong_bam):
            idx = 0
        return self.ban_do_nut[self.vong_bam[idx]]

bq_15 = BamNhatQuan()
bq_15.them_may_chu("Server_A")
bq_15.them_may_chu("Server_B")
print("Bai 15: ", f"Khoa 'data_1' thuoc ve: {bq_15.lay_may_chu('data_1')}")
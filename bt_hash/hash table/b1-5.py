# --- BÀI 1
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

bb_1 = BangBamChaining()
bb_1.put('a', 1)
print("Bai 1: ", bb_1.get('a'))


# --- BÀI 2
class BangBamDoTuyenTinh:
    def __init__(self, kich_thuoc=10):
        self.kich_thuoc = kich_thuoc
        self.cac_khoa = [None] * kich_thuoc
        self.cac_gia_tri = [None] * kich_thuoc

    def _ham_bam(self, khoa):
        return hash(khoa) % self.kich_thuoc

    def put(self, khoa, gia_tri):
        idx = self._ham_bam(khoa)
        goc = idx
        while self.cac_khoa[idx] is not None:
            if self.cac_khoa[idx] == khoa:
                self.cac_gia_tri[idx] = gia_tri
                return
            idx = (idx + 1) % self.kich_thuoc
            if idx == goc:
                raise MemoryError("Bang bam da day")
        self.cac_khoa[idx] = khoa
        self.cac_gia_tri[idx] = gia_tri

    def get(self, khoa):
        idx = self._ham_bam(khoa)
        goc = idx
        while self.cac_khoa[idx] is not None:
            if self.cac_khoa[idx] == khoa:
                return self.cac_gia_tri[idx]
            idx = (idx + 1) % self.kich_thuoc
            if idx == goc:
                break
        return None

bb_2 = BangBamDoTuyenTinh()
bb_2.put('a', 1)
print("Bai 2: ", bb_2.get('a'))


# --- BÀI 3
def dem_tan_suat(mang):
    bang_bam = {}
    for phan_tu in mang:
        if phan_tu in bang_bam:
            bang_bam[phan_tu] += 1
        else:
            bang_bam[phan_tu] = 1
    return bang_bam

mang_b3 = ['a', 'b', 'a', 'c', 'a']
print("Bai 3: ", dem_tan_suat(mang_b3))


# --- BÀI 4
def tim_phan_tu_chung(mang_1, mang_2):
    tap_hop = set(mang_1)
    ket_qua = set()
    for phan_tu in mang_2:
        if phan_tu in tap_hop:
            ket_qua.add(phan_tu)
    return ket_qua

m1 = [1, 2, 3]
m2 = [2, 3, 4]
print("Bai 4: ", tim_phan_tu_chung(m1, m2))


# --- BÀI 5
def nhom_theo_chu_cai_dau(danh_sach_tu):
    bang_nhom = {}
    for tu in danh_sach_tu:
        if not tu:
            continue
        chu_dau = tu[0]
        if chu_dau not in bang_nhom:
            bang_nhom[chu_dau] = []
        bang_nhom[chu_dau].append(tu)
    return bang_nhom

cac_tu = ["apple", "banana", "apricot", "cherry", "blueberry"]
print("Bai 5: ", nhom_theo_chu_cai_dau(cac_tu))
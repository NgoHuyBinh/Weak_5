# --- CÂU 47
def polynomial_rolling_hash(chuoi, p=31, m=1000000007):
    gia_tri_bam = 0
    for ky_tu in chuoi:
        gia_tri_bam = (gia_tri_bam * p + ord(ky_tu)) % m
    return gia_tri_bam

print("Cau 47: ", polynomial_rolling_hash("abc"))


# --- CÂU 48
def rabin_karp(van_ban, mau_tim):
    n = len(van_ban)
    m = len(mau_tim)
    p = 31
    mod = 1000000007
    
    hash_mau = 0
    hash_cua_so = 0
    p_mu_m_1 = 1
    
    # Tính trước p^(m-1) để dùng khi dịch cửa sổ
    for i in range(m - 1):
        p_mu_m_1 = (p_mu_m_1 * p) % mod
        
    # Tính mã băm ban đầu cho mẫu và cửa sổ đầu tiên
    for i in range(m):
        hash_mau = (hash_mau * p + ord(mau_tim[i])) % mod
        hash_cua_so = (hash_cua_so * p + ord(van_ban[i])) % mod
        
    # Dịch chuyển cửa sổ trên văn bản
    for i in range(n - m + 1):
        if hash_mau == hash_cua_so:
            if van_ban[i:i+m] == mau_tim:
                return i  # Trả về vị trí khớp đầu tiên
                
        # Cập nhật mã băm cho cửa sổ tiếp theo trong O(1) bằng toán thức Rolling Hash
        if i < n - m:
            hash_cua_so = (hash_cua_so - ord(van_ban[i]) * p_mu_m_1) * p + ord(van_ban[i+m])
            hash_cua_so = hash_cua_so % mod
            if hash_cua_so < 0:
                hash_cua_so += mod
                
    return -1

print("Cau 48: ", rabin_karp("zabcd", "abc"))


# --- CÂU 49
import random

class UniversalHashFamily:
    def __init__(self, m, p=1000003):
        self.m = m
        self.p = p  # p phải là số nguyên tố lớn hơn m
        self.a = random.randint(1, p - 1)
        self.b = random.randint(0, p - 1)

    def hash(self, k):
        return ((self.a * k + self.b) % self.p) % self.m

bo_bam_49 = UniversalHashFamily(10)
print("Cau 49: ", bo_bam_49.hash(12345))


# --- CÂU 50
class BloomFilter:
    def __init__(self, m, k):
        self.m = m  # Kích thước mảng bit
        self.k = k  # Số lượng hàm băm độc lập
        self.mang_bit = [0] * m

    def _cac_ham_bam(self, item):
        vi_tri = []
        for i in range(self.k):
            # Tạo các hàm băm khác nhau bằng cách kết hợp số thứ tự i vào chuỗi dữ liệu
            h = hash(f"{item}-{i}") % self.m
            vi_tri.append(h)
        return vi_tri

    def add(self, item):
        for idx in self._cac_ham_bam(item):
            self.mang_bit[idx] = 1

    def contains(self, item):
        for idx in self._cac_ham_bam(item):
            if self.mang_bit[idx] == 0:
                return False  # Chắc chắn 100% không có trong tập hợp
        return True  # Có thể có trong tập hợp (Xác suất dương tính giả)

bf = BloomFilter(20, 3)
bf.add("apple")
print("Cau 50: ", f"Chua 'apple': {bf.contains('apple')} | Chua 'banana': {bf.contains('banana')}")
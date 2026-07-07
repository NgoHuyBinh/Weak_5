# --- BÀI 11
def ham_bam_doc_lap_thu_tu(tap_hop, m):
    gia_tri_hash_tong = 0
    for phan_tu in tap_hop:
        gia_tri_hash_tong ^= hash(phan_tu)
    return gia_tri_hash_tong % m

t1 = {1, 2, 3}
t2 = {3, 1, 2}
kq_t1 = ham_bam_doc_lap_thu_tu(t1, 10)
kq_t2 = ham_bam_doc_lap_thu_tu(t2, 10)
print("Bai 11: ", f"t1: {kq_t1} | t2: {kq_t2}")


# --- BÀI 12
import hmac
import hashlib

class BangBamBaoMat:
    def __init__(self, m):
        self.m = m
        self.cac_o = [[] for _ in range(m)]
        self.khoa_bi_mat = b'secret_key_random'

    def _ham_bam_bao_mat(self, khoa):
        chuoi_khoa = str(khoa).encode('utf-8')
        chuoi_mac = hmac.new(self.khoa_bi_mat, chuoi_khoa, hashlib.sha256).hexdigest()
        return int(chuoi_mac, 16) % self.m

    def put(self, khoa, gia_tri):
        idx = self._ham_bam_bao_mat(khoa)
        for cap in self.cac_o[idx]:
            if cap[0] == khoa:
                cap[1] = gia_tri
                return
        self.cac_o[idx].append([khoa, gia_tri])

    def get(self, khoa):
        idx = self._ham_bam_bao_mat(khoa)
        for cap in self.cac_o[idx]:
            if cap[0] == khoa:
                return cap[1]
        return None

bb_12 = BangBamBaoMat(10)
bb_12.put('user1', 'data1')
print("Bai 12: ", bb_12.get('user1'))


# --- BÀI 13
def rolling_hash_2d(ma_tran, r_con, c_con):
    R = len(ma_tran)
    C = len(ma_tran[0])
    p = 31
    q = 37
    mod = 1000000007

    p_mu = [1] * C
    for j in range(1, C):
        p_mu[j] = (p_mu[j-1] * p) % mod

    hash_dong = [[0] * C for _ in range(R)]
    for i in range(R):
        current_hash = 0
        for j in range(c_con):
            current_hash = (current_hash * p + ma_tran[i][j]) % mod
        hash_dong[i][0] = current_hash
        
        for j in range(1, C - c_con + 1):
            current_hash = (current_hash - ma_tran[i][j-1] * p_mu[c_con-1]) * p + ma_tran[i][j+c_con-1]
            hash_dong[i][j] = current_hash % mod

    q_mu_r = 1
    for i in range(r_con - 1):
        q_mu_r = (q_mu_r * q) % mod

    hash_2d = [[0] * (C - c_con + 1) for _ in range(R - r_con + 1)]
    for j in range(C - c_con + 1):
        current_hash = 0
        for i in range(r_con):
            current_hash = (current_hash * q + hash_dong[i][j]) % mod
        hash_2d[0][j] = current_hash
        
        for i in range(1, R - r_con + 1):
            current_hash = (current_hash - hash_dong[i-1][j] * q_mu_r) * q + hash_dong[i+r_con-1][j]
            hash_2d[i][j] = current_hash % mod
            
    return hash_2d

mt_lon = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
kq_b13 = rolling_hash_2d(mt_lon, 2, 2)
print("Bai 13: ", f"Ma tran hash 2D tai cac o cua so: {kq_b13}")


# --- BÀI 14
class BloomFilter:
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.mang_bit = [0] * m

    def _cac_ham_bam(self, item):
        vi_tri = []
        for i in range(self.k):
            h = hash(f"{item}-{i}") % self.m
            vi_tri.append(h)
        return vi_tri

    def add(self, item):
        for idx in self._cac_ham_bam(item):
            self.mang_bit[idx] = 1

    def contains(self, item):
        for idx in self._cac_ham_bam(item):
            if self.mang_bit[idx] == 0:
                return False
        return True

bf = BloomFilter(20, 3)
bf.add("apple")
print("Bai 14: ", f"Chua 'apple': {bf.contains('apple')} | Chua 'banana': {bf.contains('banana')}")


# --- BÀI 15
def uoc_luong_minhash(tap_a, tap_b, so_ham_hash=100):
    minhash_a = []
    minhash_b = []
    p = 1000003
    
    for i in range(so_ham_hash):
        min_a = float('inf')
        min_b = float('inf')
        
        for phan_tu in tap_a:
            h = (hash(phan_tu) * (i + 1) + 13) % p
            if h < min_a: min_a = h
        for phan_tu in tap_b:
            h = (hash(phan_tu) * (i + 1) + 13) % p
            if h < min_b: min_b = h
            
        minhash_a.append(min_a)
        minhash_b.append(min_b)
        
    khop = 0
    for i in range(so_ham_hash):
        if minhash_a[i] == minhash_b[i]:
            khop += 1
            
    return khop / so_ham_hash

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}
kq_b15 = uoc_luong_minhash(set_a, set_b)
print("Bai 15: ", f"Do tuong dong Jaccard uoc luong: {kq_b15}")
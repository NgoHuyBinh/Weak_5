# --- BÀI 6
def rabin_karp(van_ban, mau_tim):
    n = len(van_ban)
    m = len(mau_tim)
    p = 31
    mod = 1000000007
    
    hash_mau = 0
    hash_cua_so = 0
    p_mu_m_1 = 1
    
    for i in range(m - 1):
        p_mu_m_1 = (p_mu_m_1 * p) % mod
        
    for i in range(m):
        hash_mau = (hash_mau * p + ord(mau_tim[i])) % mod
        hash_cua_so = (hash_cua_so * p + ord(van_ban[i])) % mod
        
    for i in range(n - m + 1):
        if hash_mau == hash_cua_so:
            if van_ban[i:i+m] == mau_tim:
                return i
                
        if i < n - m:
            hash_cua_so = (hash_cua_so - ord(van_ban[i]) * p_mu_m_1) * p + ord(van_ban[i+m])
            hash_cua_so = hash_cua_so % mod
            if hash_cua_so < 0:
                hash_cua_so += mod
                
    return -1

kq_bai_6 = rabin_karp('zabcd', 'abc')
print("Bai 6: ", kq_bai_6)


# --- BÀI 7
def hash_combine(cap_ab, m):
    a, b = cap_ab
    h_a = hash(a)
    h_b = hash(b)
    h_ket_hop = h_a ^ (h_b + 0x9e3779b9 + (h_a << 6) + (h_a >> 2))
    return h_ket_hop % m

kq_bai_7 = hash_combine(('x', 'y'), 10)
print("Bai 7: ", kq_bai_7)


# --- BÀI 8
def tinh_do_lech_chi_square(cac_bucket, tong_so_khoa):
    m = len(cac_bucket)
    ky_vong = tong_so_khoa / m
    chi_square = 0.0
    for so_luong in cac_bucket:
        chi_square += ((so_luong - ky_vong) ** 2) / ky_vong
    return chi_square

bucket_ham_1 = [10, 11, 9, 10]
bucket_ham_2 = [18, 2, 15, 5]
do_lech_1 = tinh_do_lech_chi_square(bucket_ham_1, 40)
do_lech_2 = tinh_do_lech_chi_square(bucket_ham_2, 40)
print("Bai 8: ", f"Do lech ham 1: {do_lech_1} | Do lech ham 2: {do_lech_2}")


# --- BÀI 9
import random

class UniversalHash:
    def __init__(self, m, p=1000003):
        self.m = m
        self.p = p
        self.a = random.randint(1, p - 1)
        self.b = random.randint(0, p - 1)

    def hash(self, k):
        return ((self.a * k + self.b) % self.p) % self.m

bo_bam_9 = UniversalHash(10)
kq_bai_9 = bo_bam_9.hash(12345)
print("Bai 9: ", kq_bai_9)


# --- BÀI 10
import math

def ham_bam_phuong_phap_nhan(k, m):
    A = 0.6180339887  
    phan_phan_so = (k * A) % 1
    return math.floor(m * phan_phan_so)

kq_bai_10 = ham_bam_phuong_phap_nhan(123456, 100)
print("Bai 10: ", kq_bai_10)
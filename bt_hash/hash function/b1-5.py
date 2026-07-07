# --- BÀI 1
def ham_bam_modulo(k, m):
    return k % m

kq_bai_1 = ham_bam_modulo(37, 10)
print("Bai 1: ", kq_bai_1)


# --- BÀI 2
def ham_bam_tong_ky_tu(chuoi, m):
    tong_ma = 0
    for ky_tu in chuoi:
        tong_ma += ord(ky_tu)
    return tong_ma % m

kq_abc = ham_bam_tong_ky_tu('abc', 10)
kq_cba = ham_bam_tong_ky_tu('cba', 10)
print("Bai 2: ", f"abc: {kq_abc} | cba: {kq_cba}")


# --- BÀI 3
def ham_bam_da_thuc(chuoi, p, m):
    gia_tri_bam = 0
    for ky_tu in chuoi:
        gia_tri_bam = (gia_tri_bam * p + ord(ky_tu)) % m
    return gia_tri_bam

kq_bai_3 = ham_bam_da_thuc('abc', 31, 1000000007)
print("Bai 3: ", kq_bai_3)


# --- BÀI 4
def dem_va_cham_ham_bam(danh_sach_khoa, m):
    cac_bucket = {}
    for khoa in danh_sach_khoa:
        idx = hash(khoa) % m
        if idx in cac_bucket:
            cac_bucket[idx] += 1
        else:
            cac_bucket[idx] = 1
            
    so_va_cham = 0
    for idx in cac_bucket:
        if cac_bucket[idx] > 1:
            so_va_cham += (cac_bucket[idx] - 1)
            
    return so_va_cham

tap_khoa = ["apple", "banana", "cherry", "date", "elderberry"]
kq_bai_4 = dem_va_cham_ham_bam(tap_khoa, 3)
print("Bai 4: ", kq_bai_4)


# --- BÀI 5
def mo_phong_phan_bo_m(danh_sach_khoa, m):
    cac_bucket = {i: 0 for i in range(m)}
    for khoa in danh_sach_khoa:
        idx = khoa % m
        cac_bucket[idx] += 1
    return cac_bucket

cac_khoa_mau = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
phan_bo_m16 = mo_phong_phan_bo_m(cac_khoa_mau, 16)
phan_bo_m17 = mo_phong_phan_bo_m(cac_khoa_mau, 17)
print("Bai 5: ", f"Phan bo voi m=16 (luy thua cua 2): {phan_bo_m16} | Phan bo voi m=17 (so nguyen to): {phan_bo_m17}")
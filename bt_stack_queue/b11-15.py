#BAI 11
def phan_tu_lon_hon_ke_tiep(mang_a):
    ket_qua = [-1] * len(mang_a)
    ngan_xep = []
    for i in range(len(mang_a)):
        while ngan_xep and mang_a[ngan_xep[-1]] < mang_a[i]:
            vi_tri = ngan_xep.pop()
            ket_qua[vi_tri] = mang_a[i]
        ngan_xep.append(i)
    return ket_qua

mang_bai_11 = [2, 1, 3]
kq_bai_11 = phan_tu_lon_hon_ke_tiep(mang_bai_11)
print("Bai 11: ", kq_bai_11)

#BAI 12
def hinh_chu_nhat_lon_nhat_histogram(chieu_cao):
    ngan_xep = []
    dien_tich_max = 0
    i = 0
    while i < len(chieu_cao):
        if not ngan_xep or chieu_cao[ngan_xep[-1]] <= chieu_cao[i]:
            ngan_xep.append(i)
            i += 1
        else:
            top = ngan_xep.pop()
            chieu_rong = i if not ngan_xep else i - ngan_xep[-1] - 1
            dien_tich_max = max(dien_tich_max, chieu_cao[top] * chieu_rong)
            
    while ngan_xep:
        top = ngan_xep.pop()
        chieu_rong = i if not ngan_xep else i - ngan_xep[-1] - 1
        dien_tich_max = max(dien_tich_max, chieu_cao[top] * chieu_rong)
        
    return dien_tich_max

mang_bai_12 = [2, 1, 5, 6, 2, 3]
kq_bai_12 = hinh_chu_nhat_lon_nhat_histogram(mang_bai_12)
print("Bai 12: ", kq_bai_12)

#BAI 13
def dfs_khu_de_quy(do_thi, dinh_dau):
    danh_dau = set()
    ngan_xep = [dinh_dau]
    ket_qua_duyet = []
    
    while ngan_xep:
        u = ngan_xep.pop()
        if u not in danh_dau:
            danh_dau.add(u)
            ket_qua_duyet.append(u)
            for v in reversed(do_thi[u]):
                if v not in danh_dau:
                    ngan_xep.append(v)
    return ket_qua_duyet

do_thi_bai_13 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
kq_bai_13 = dfs_khu_de_quy(do_thi_bai_13, 'A')
print("Bai 13: ", kq_bai_13)

#BAI 14
def bai_toan_nhip_gia_co_phieu(gia):
    nhip_gia = [0] * len(gia)
    ngan_xep = []
    for i in range(len(gia)):
        while ngan_xep and gia[ngan_xep[-1]] <= gia[i]:
            ngan_xep.pop()
        nhip_gia[i] = i + 1 if not ngan_xep else i - ngan_xep[-1]
        ngan_xep.append(i)
    return nhip_gia

mang_bai_14 = [100, 80, 60, 70, 60, 75, 85]
kq_bai_14 = bai_toan_nhip_gia_co_phieu(mang_bai_14)
print("Bai 14: ", kq_bai_14)

#BAI 15
def sap_xep_ngan_xep(ngan_xep_goc):
    ngan_xep_phu = []
    while ngan_xep_goc:
        tam = ngan_xep_goc.pop()
        while ngan_xep_phu and ngan_xep_phu[-1] > tam:
            ngan_xep_goc.append(ngan_xep_phu.pop())
        ngan_xep_phu.append(tam)
    return ngan_xep_phu

stack_bai_15 = [3, 1, 2]
kq_bai_15 = sap_xep_ngan_xep(stack_bai_15)
print("Bai 15: ", kq_bai_15)
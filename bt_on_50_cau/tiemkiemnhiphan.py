# --- CÂU 1
def tim_kiem_co_ban(mang, x):
    trai = 0
    phai = len(mang) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] == x:
            return giua
        elif mang[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return -1

mang_c1 = [1, 3, 5, 7, 9]
print("Bai 1: ", tim_kiem_co_ban(mang_c1, 7))


# --- CÂU 2
def vi_tri_dau_cuoi_dem(mang, x):
    def tim_dau():
        trai, phai = 0, len(mang) - 1
        kq = -1
        while trai <= phai:
            giua = (trai + phai) // 2
            if mang[giua] == x:
                kq = giua
                phai = giua - 1
            elif mang[giua] < x:
                trai = giua + 1
            else:
                phai = giua - 1
        return kq

    def tim_cuoi():
        trai, phai = 0, len(mang) - 1
        kq = -1
        while trai <= phai:
            giua = (trai + phai) // 2
            if mang[giua] == x:
                kq = giua
                trai = giua + 1
            elif mang[giua] < x:
                trai = giua + 1
            else:
                phai = giua - 1
        return kq

    dau = tim_dau()
    if dau == -1:
        return -1, -1, 0
    cuoi = tim_cuoi()
    dem = cuoi - dau + 1
    return dau, cuoi, dem

mang_c2 = [1, 2, 2, 2, 3]
print("Bai 2: ", vi_tri_dau_cuoi_dem(mang_c2, 2))


# --- CÂU 3
def lower_upper_bound(mang, x):
    def lower_bound():
        trai, phai = 0, len(mang) - 1
        kq = len(mang)
        while trai <= phai:
            giua = (trai + phai) // 2
            if mang[giua] >= x:
                kq = giua
                phai = giua - 1
            else:
                trai = giua + 1
        return kq

    def upper_bound():
        trai, phai = 0, len(mang) - 1
        kq = len(mang)
        while trai <= phai:
            giua = (trai + phai) // 2
            if mang[giua] > x:
                kq = giua
                phai = giua - 1
            else:
                trai = giua + 1
        return kq

    return lower_bound(), upper_bound()

mang_c3 = [1, 3, 5, 7]
print("Bai 3: ", lower_upper_bound(mang_c3, 4))


# --- CÂU 4
def tim_trong_mang_xoay(mang, x):
    trai = 0
    phai = len(mang) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] == x:
            return giua
        
        if mang[trai] <= mang[giua]:
            if mang[trai] <= x < mang[giua]:
                phai = giua - 1
            else:
                trai = giua + 1
        else:
            if mang[giua] < x <= mang[phai]:
                trai = giua + 1
            else:
                phai = giua - 1
    return -1

mang_c4 = [4, 5, 6, 7, 0, 1, 2]
print("Bai 4: ", tim_trong_mang_xoay(mang_c4, 0))


# --- CÂU 5
import math

def koko_an_chuoi(cac_dong, h):
    def kiem_tra(toc_do):
        tong_gio = 0
        for dong in cac_dong:
            tong_gio += math.ceil(dong / toc_do)
        return tong_gio <= h

    trai = 1
    phai = max(cac_dong)
    kq = phai
    
    while trai <= phai:
        giua = (trai + phai) // 2
        if kiem_tra(giua):
            kq = giua
            phai = giua - 1
        else:
            trai = giua + 1
    return kq

dong_chuoi = [3, 6, 7, 11]
print("Bai 5: ", koko_an_chuoi(dong_chuoi, 8))


# --- CÂU 6
def chia_mang_tong_min_max(mang, k):
    def kiem_tra(tong_muc_tieu):
        so_doan = 1
        tong_hien_tai = 0
        for phan_tu in mang:
            if tong_hien_tai + phan_tu > tong_muc_tieu:
                so_doan += 1
                tong_hien_tai = phan_tu
                if so_doan > k:
                    return False
            else:
                tong_hien_tai += phan_tu
        return True

    trai = max(mang)
    phai = sum(mang)
    kq = phai
    
    while trai <= phai:
        giua = (trai + phai) // 2
        if kiem_tra(giua):
            kq = giua
            phai = giua - 1
        else:
            trai = giua + 1
    return kq

mang_c6 = [7, 2, 5, 10, 8]
print("Bai 6: ", chia_mang_tong_min_max(mang_c6, 2))
# --- CÂU 7
def bubble_sort_dem_swap(mang):
    a = mang.copy()
    n = len(a)
    so_swap = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                so_swap += 1
    return so_swap

mang_c7 = [2, 3, 1]
print("Bai 7: ", bubble_sort_dem_swap(mang_c7))


# --- CÂU 8
def bubble_sort_toi_uu(mang):
    a = mang.copy()
    n = len(a)
    so_luot = 0
    for i in range(n):
        so_luot += 1
        co_swap = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                co_swap = True
        if not co_swap:
            break
    return so_luot

mang_c8 = [1, 2, 3, 4]
print("Bai 8: ", bubble_sort_toi_uu(mang_c8))


# --- CÂU 9
def insertion_sort_dem_shift(mang):
    a = mang.copy()
    n = len(a)
    tong_shift = 0
    for i in range(1, n):
        khoa = a[i]
        j = i - 1
        while j >= 0 and a[j] > khoa:
            a[j + 1] = a[j]
            j -= 1
            tong_shift += 1
        a[j + 1] = khoa
    return tong_shift

mang_c9 = [3, 2, 1]
print("Bai 9: ", insertion_sort_dem_shift(mang_c9))


# --- CÂU 10
def binary_insertion_sort(mang):
    a = mang.copy()
    n = len(a)
    for i in range(1, n):
        khoa = a[i]
        trai = 0
        phai = i - 1
        while trai <= phai:
            giua = (trai + phai) // 2
            if a[giua] > khoa:
                phai = giua - 1
            else:
                trai = giua + 1
        for j in range(i - 1, trai - 1, -1):
            a[j + 1] = a[j]
        a[trai] = khoa
    return a

mang_c10 = [3, 2, 1]
print("Bai 10: ", binary_insertion_sort(mang_c10))


# --- CÂU 11
def selection_sort_dem_so_sanh(mang):
    a = mang.copy()
    n = len(a)
    so_so_sanh = 0
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            so_so_sanh += 1
            if a[j] < a[idx_min]:
                idx_min = j
        a[i], a[idx_min] = a[idx_min], a[i]
    return so_so_sanh

mang_c11 = [5, 4, 3, 2, 1]
print("Bai 11: ", selection_sort_dem_so_sanh(mang_c11))


# --- CÂU 12
def minh_hoa_selection_sort_mat_on_dinh():
    a = [(2, 'x'), (2, 'y'), (1, 'z')]
    n = len(a)
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            if a[j][0] < a[idx_min][0]:
                idx_min = j
        a[i], a[idx_min] = a[idx_min], a[i]
    return a

print("Bai 12: ", minh_hoa_selection_sort_mat_on_dinh())


# --- CÂU 13
def dem_nghich_the_merge_sort(mang):
    def merge_and_count(a, tam, trai, giua, phai):
        i = trai
        j = giua + 1
        k = trai
        dem = 0
        while i <= giua and j <= phai:
            if a[i] <= a[j]:
                tam[k] = a[i]
                i += 1
            else:
                tam[k] = a[j]
                dem += (giua - i + 1)
                j += 1
            k += 1
        while i <= giua:
            tam[k] = a[i]
            i += 1
            k += 1
        while j <= phai:
            tam[k] = a[j]
            j += 1
            k += 1
        for chi_so in range(trai, phai + 1):
            a[chi_so] = tam[chi_so]
        return dem

    def _merge_sort(a, tam, trai, phai):
        dem = 0
        if trai < phai:
            giua = (trai + phai) // 2
            dem += _merge_sort(a, tam, trai, giua)
            dem += _merge_sort(a, tam, giua + 1, phai)
            dem += merge_and_count(a, tam, trai, giua, phai)
        return dem

    mang_copy = mang.copy()
    mang_tam = [0] * len(mang_copy)
    return _merge_sort(mang_copy, mang_tam, 0, len(mang_copy) - 1)

mang_c13 = [1, 20, 6, 4, 5]
print("Bai 13: ", dem_nghich_the_merge_sort(mang_c13))


# --- CÂU 14
def shell_sort_dem_shift(mang, cac_gap):
    a = mang.copy()
    n = len(a)
    tong_shift = 0
    for gap in cac_gap:
        for i in range(gap, n):
            khoa = a[i]
            j = i
            while j >= gap and a[j - gap] > khoa:
                a[j] = a[j - gap]
                j -= gap
                tong_shift += 1
            a[j] = khoa
    return tong_shift

mang_c14 = [9, 8, 3, 7, 5, 6, 4, 1]
day_gap = [4, 2, 1]
print("Bai 14: ", shell_sort_dem_shift(mang_c14, day_gap))
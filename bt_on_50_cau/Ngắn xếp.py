# --- CÂU 21
def kiem_tra_ngoac_can_bang(chuoi):
    ngan_xep = []
    ban_do_ngoac = {')': '(', ']': '[', '}': '{'}
    
    for ky_tu in chuoi:
        if ky_tu in ban_do_ngoac.values():
            ngan_xep.append(ky_tu)
        elif ky_tu in ban_do_ngoac.keys():
            if not ngan_xep or ngan_xep[-1] != ban_do_ngoac[ky_tu]:
                return False
            ngan_xep.pop()
            
    return len(ngan_xep) == 0

print("Cau 21: ", kiem_tra_ngoac_can_bang("([{}])"))


# --- CÂU 22
class MinStack:
    def __init__(self):
        self.ngan_xep_chinh = []
        self.ngan_xep_min = []

    def push(self, gia_tri):
        self.ngan_xep_chinh.append(gia_tri)
        if not self.ngan_xep_min or gia_tri <= self.ngan_xep_min[-1]:
            self.ngan_xep_min.append(gia_tri)

    def pop(self):
        if not self.ngan_xep_chinh:
            return None
        gia_tri_xoa = self.ngan_xep_chinh.pop()
        if gia_tri_xoa == self.ngan_xep_min[-1]:
            self.ngan_xep_min.pop()
        return gia_tri_xoa

    def top(self):
        return self.ngan_xep_chinh[-1] if self.ngan_xep_chinh else None

    def getMin(self):
        return self.ngan_xep_min[-1] if self.ngan_xep_min else None

stack_22 = MinStack()
stack_22.push(5)
stack_22.push(3)
stack_22.push(7)
print("Cau 22: ", stack_22.getMin())


# --- CÂU 23
def tinh_bieu_thuc_hau_to(bieu_thuc):
    ngan_xep = []
    cac_phan_tu = bieu_thuc.split()
    
    for phan_tu in cac_phan_tu:
        if phan_tu not in ['+', '-', '*', '/']:
            ngan_xep.append(int(phan_tu))
        else:
            b = ngan_xep.pop()
            a = ngan_xep.pop()
            if phan_tu == '+': ngan_xep.append(a + b)
            elif phan_tu == '-': ngan_xep.append(a - b)
            elif phan_tu == '*': ngan_xep.append(a * b)
            elif phan_tu == '/': ngan_xep.append(int(a / b))  # Lấy phần nguyên theo đề bài
            
    return ngan_xep[0] if ngan_xep else 0

print("Cau 23: ", tinh_bieu_thuc_hau_to("3 4 + 2 *"))


# --- CÂU 24
def phan_tu_lon_hon_tiep_theo(mang):
    n = len(mang)
    ket_qua = [-1] * n
    ngan_xep_don_dieu = []  # Lưu chỉ số (index) của các phần tử
    
    for i in range(n):
        while ngan_xep_don_dieu and mang[ngan_xep_don_dieu[-1]] < mang[i]:
            idx_truoc = ngan_xep_don_dieu.pop()
            ket_qua[idx_truoc] = mang[i]
        ngan_xep_don_dieu.append(i)
        
    return ket_qua

print("Cau 24: ", phan_tu_lon_hon_tiep_theo([2, 1, 3]))


# --- CÂU 25
def dien_tich_histogram_lon_nhat(chieu_cao):
    ngan_xep = []  # Lưu chỉ số (index)
    dien_tich_max = 0
    n = len(chieu_cao)
    
    for i in range(n + 1):
        # Dùng một cột giả có chiều cao = 0 ở cuối để vét nốt các phần tử còn lại trong stack
        h_hien_tai = chieu_cao[i] if i < n else 0
        
        while ngan_xep and chieu_cao[ngan_xep[-1]] > h_hien_tai:
            h_cot = chieu_cao[ngan_xep.pop()]
            chieu_rong = i if not ngan_xep else i - ngan_xep[-1] - 1
            dien_tich_max = max(dien_tich_max, h_cot * chieu_rong)
            
        ngan_xep.append(i)
        
    return dien_tich_max

print("Cau 25: ", dien_tich_histogram_lon_nhat([2, 1, 5, 6, 2, 3]))
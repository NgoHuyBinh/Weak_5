from collections import deque

#BAI 6
def kiem_tra_ngoac_can_bang(chuoi_ngoac):
    ngan_xep = []
    cap_ngoac = {')': '(', ']': '[', '}': '{'}
    for ky_tu in chuoi_ngoac:
        if ky_tu in cap_ngoac.values():
            ngan_xep.append(ky_tu)
        elif ky_tu in cap_ngoac:
            if not ngan_xep or ngan_xep.pop() != cap_ngoac[ky_tu]:
                return False
    return len(ngan_xep) == 0

kq_bai_6 = kiem_tra_ngoac_can_bang("(([]{}))")
print("Bai 6: ", kq_bai_6)

#BAI 7
class NganXepMin:
    def __init__(self):
        self.ngan_xep_chinh = []
        self.ngan_xep_min = []
        
    def day_vao(self, gia_tri):
        self.ngan_xep_chinh.append(gia_tri)
        if not self.ngan_xep_min or gia_tri <= self.ngan_xep_min[-1]:
            self.ngan_xep_min.append(gia_tri)
            
    def lay_ra(self):
        if self.ngan_xep_chinh:
            gia_tri = self.ngan_xep_chinh.pop()
            if gia_tri == self.ngan_xep_min[-1]:
                self.ngan_xep_min.pop()
            return gia_tri
        return None
        
    def lay_min(self):
        if self.ngan_xep_min:
            return self.ngan_xep_min[-1]
        return None

nx_min = NganXepMin()
nx_min.day_vao(5)
nx_min.day_vao(3)
nx_min.day_vao(7)
kq_bai_7 = nx_min.lay_min()
print("Bai 7: ", kq_bai_7)

#BAI 8
def tinh_bieu_thuc_hau_to(bieu_thuc):
    ngan_xep = []
    cac_phan_tu = bieu_thuc.split()
    for phan_tu in cac_phan_tu:
        if phan_tu.isdigit():
            ngan_xep.append(int(phan_tu))
        else:
            b = ngan_xep.pop()
            a = ngan_xep.pop()
            if phan_tu == '+': ngan_xep.append(a + b)
            elif phan_tu == '-': ngan_xep.append(a - b)
            elif phan_tu == '*': ngan_xep.append(a * b)
            elif phan_tu == '/': ngan_xep.append(int(a / b))
    return ngan_xep[0]

kq_bai_8 = tinh_bieu_thuc_hau_to("3 4 + 2 *")
print("Bai 8: ", kq_bai_8)

#BAI 9
def trung_to_sang_hau_to(bieu_thuc):
    do_uu_tien = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    ngan_xep = []
    ket_qua = []
    for ky_tu in bieu_thuc:
        if ky_tu.isalnum():
            ket_qua.append(ky_tu)
        elif ky_tu == '(':
            ngan_xep.append(ky_tu)
        elif ky_tu == ')':
            while ngan_xep and ngan_xep[-1] != '(':
                ket_qua.append(ngan_xep.pop())
            ngan_xep.pop()
        elif ky_tu in do_uu_tien:
            while ngan_xep and ngan_xep[-1] != '(' and do_uu_tien.get(ngan_xep[-1], 0) >= do_uu_tien[ky_tu]:
                ket_qua.append(ngan_xep.pop())
            ngan_xep.append(ky_tu)
    while ngan_xep:
        ket_qua.append(ngan_xep.pop())
    return " ".join(ket_qua)

kq_bai_9 = trung_to_sang_hau_to("a+b*c")
print("Bai 9: ", kq_bai_9)

#BAI 10
class NganXepBangHangDoi:
    def __init__(self):
        self.hang_doi_1 = deque()
        self.hang_doi_2 = deque()
        
    def day_vao(self, gia_tri):
        self.hang_doi_2.append(gia_tri)
        while self.hang_doi_1:
            self.hang_doi_2.append(self.hang_doi_1.popleft())
        self.hang_doi_1, self.hang_doi_2 = self.hang_doi_2, self.hang_doi_1
        
    def lay_ra(self):
        if self.hang_doi_1:
            return self.hang_doi_1.popleft()
        return None

nx_hd = NganXepBangHangDoi()
nx_hd.day_vao(5)
nx_hd.day_vao(7)
kq_bai_10 = nx_hd.lay_ra()
print("Bai 10: ", kq_bai_10)
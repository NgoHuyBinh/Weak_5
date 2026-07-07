# --- BÀI 1
class ArrayListCoBan:
    def __init__(self):
        self.mang = []
        
    def add(self, gia_tri):
        self.mang.append(gia_tri)
        
    def get(self, chi_so):
        return self.mang[chi_so]
        
    def set(self, chi_so, gia_tri):
        self.mang[chi_so] = gia_tri
        
    def size(self):
        return len(self.mang)

ds_bai_1 = ArrayListCoBan()
ds_bai_1.add(1)
ds_bai_1.add(2)
ds_bai_1.add(3)
kq_bai_1 = ds_bai_1.get(1)
print("Bai 1: ", kq_bai_1)


# --- BÀI 2
class ArrayListThemXoaCuoi:
    def __init__(self):
        self.mang = [1, 2, 3]
        
    def append(self, gia_tri):
        self.mang.append(gia_tri)
        
    def popBack(self):
        return self.mang.pop()

ds_bai_2 = ArrayListThemXoaCuoi()
kq_bai_2 = ds_bai_2.popBack()
print("Bai 2: ", kq_bai_2)


# --- BÀI 3
class ArrayListChenXoaViTri:
    def __init__(self):
        self.mang = [1, 2, 4]
        
    def chen_tai_idx(self, chi_so, gia_tri):
        self.mang.insert(chi_so, gia_tri)
        
    def xoa_tai_idx(self, chi_so):
        return self.mang.pop(chi_so)

ds_bai_3 = ArrayListChenXoaViTri()
ds_bai_3.chen_tai_idx(2, 3)
print("Bai 3: ", ds_bai_3.mang)


# --- BÀI 4
class ArrayListTimKiem:
    def __init__(self):
        self.mang = [5, 3, 7]
        
    def indexOf(self, gia_tri):
        for i in range(len(self.mang)):
            if self.mang[i] == gia_tri:
                return i
        return -1

ds_bai_4 = ArrayListTimKiem()
kq_bai_4 = ds_bai_4.indexOf(7)
print("Bai 4: ", kq_bai_4)


# --- BÀI 5
class ArrayListDuyet:
    def __init__(self):
        self.mang = [1, 2, 3, 4]
        
    def duyet_va_dem_so_chan(self):
        dem_so_chan = 0
        for gia_tri in self.mang:
            if gia_tri % 2 == 0:
                dem_so_chan += 1
        return dem_so_chan

ds_bai_5 = ArrayListDuyet()
kq_bai_5 = ds_bai_5.duyet_va_dem_so_chan()
print("Bai 5: ", kq_bai_5)
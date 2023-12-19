s = "ĐHSP Kỹ thuật Hƣng Yên"

st = input('Nhập chuỗi : ').strip()

if (s.find(st) != -1):
    print(f'Chuỗi {st} nằm trong chuỗi {s}')
else :
    print(f'Chuỗi {st} không nằm trong {s}')
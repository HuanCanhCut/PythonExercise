# 2.8 trang 72

s = input('s = ').strip()

c = input('c = ').strip()

if c in s :
    count = s.count(c)
    print(f'{c} xuat hien trong {s} {count} lan')
else :
    print(f'{c} khong xuat hien trong {s}')
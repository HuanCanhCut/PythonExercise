L = []

n = int(input('Nhập một số nguyên dương n: '))

for i in range(1, n + 1):
    x = float(input(f'Vui lòng nhập các giá trị x{i}: '))
    L.append(x)

print(f'\n Giá trị lớn nhất trong danh sách trên là {max(L)}')
print(f'Tổng các phần tử trong danh sách trên là {sum(L)}')
print(f'Các phần tử theo thứ tự tăng dần trong danh sách trên là {sorted(L)}')

soAm = 0
soDuong = 0

for i in L:
    if (i < 0) :
        soAm += 1

    if (i > 0) :
        soDuong += 1

print(f'Trong danh sách có {soAm} số âm và {soDuong} số dương')

for i in L :
    print(i)
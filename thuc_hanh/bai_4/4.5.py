# Thuật toán euclid

def UCLN (a, b):

    while (b != 0):
        phanDu = a % b
        a = b
        b = phanDu
    return a


a = int(input('Vui lòng nhập số thứ nhất : '))
b = int(input('Vui lòng nhập số thứ hai : '))

print(f'Ước chung lớn nhât của {a} và {b} là : {UCLN(a, b)}')
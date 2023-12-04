thang31 = [1, 3, 5, 7, 8, 10, 12]
thang30 = [4, 6, 9, 11]

thang = int(input('Nhập vào tháng: ').strip())
nam = int(input('Nhập vào năm: ').strip())

if thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0):
        print('Tháng 2 có 29 ngày')
    else :
        print('Tháng 2 có 28 ngày')
else:
    if thang in thang30:
        print(f'Tháng {thang} có 30 ngày')
    elif thang in thang31:
        print(f'Tháng {thang} có 31 ngày')
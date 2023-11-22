while (True):
    thang = input('Nhập vào tháng: ').strip()
    if (thang.isdigit() or int(thang) != 0) :
        thang = int(thang)
        if (thang >= 2 and thang <= 4):
            ketQua = 'Mùa xuân'
        elif (thang >= 5 and thang <= 7):
            ketQua = 'Mùa hạ'
        elif (thang >= 8 and thang <= 10):
            ketQua = 'Mùa thu'
        else :
            ketQua = 'Mùa đông'
        print(f'Tháng {thang} là : {ketQua}')
        break
    else :
        print('Tháng nhập vào phải là số nguyên dương nhỏ hơn 12 và lớn hơn 0!, vui lòng nhập lại \n')
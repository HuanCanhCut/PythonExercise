while (True):
    a = input('Vui lòng nhập số thứ nhất : ')
    b = input('Vui lòng nhập số thứ hai : ')
    
    if(a.isdigit() and b.isdigit()):
        a = int(a)
        b = int(b)
        while (b != 0):
            phanDu = a % b
            a = b
            b = phanDu
        print(f'UCLN của hai số là : {a}')
        break
    else :
        print('Vui lòng nhập hai số là số nguyên dương!')
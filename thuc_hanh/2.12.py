while(True):
    n = input('Nhập vào số nguyên dương: ').strip()
    if(n.isdigit() and int(n) != 0 and int(n) <= 100):
        n = int(n)
        s = 0
        for i in range(1, n + 1):
            if (i % 2 == 0):
                s = s + i
        print(f'Tổng các số chẵn từ 1 => 100 = {s}')
        break
    else :
        print('Giá trị nhập vào phải là số nguyên dương lớn hơn 0 và nhỏ hơn hoặc bằng 100. Vui lòng nhập lại')
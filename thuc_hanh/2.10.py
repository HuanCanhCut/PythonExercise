import math

while (True):
    a = input('Nhập vào cạnh thứ nhất: ')
    b = input('Nhập vào cạnh thứ hai: ')
    c = input('Nhập vào cạnh thứ ba: ')

    if(a.isdigit() and b.isdigit() and c.isdigit()):
        # ép kiểu của dữ liệu sau khi thỏa mãn điều kiện số nguyên dương
        a = float(a)
        b = float(b)
        c = float(c)

        if(a + b > c and a + c > b and b + c > a ):
            nuaChuvi = (a + b + c ) / 2
            dienTich = math.sqrt(nuaChuvi * (nuaChuvi - a) * (nuaChuvi - b) * (nuaChuvi - c))
            print(f'Ba cạnh vừa nhập là 3 cạnh của một tam giác và có diện tích là : {dienTich}')
            break
    else :
        print('3 cạnh của một tam giác phải là số nguyên dương, Vui lòng nhập lại \n')
    
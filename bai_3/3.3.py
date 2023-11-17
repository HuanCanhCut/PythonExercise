import math
from regex import floatRegex


while(True):
    a = input('Vui lòng nhập vào tham số thứ nhất : ').strip()
    b = input('Vui lòng nhập vào tham số thứ hai : ').strip()
    c = input('Vui lòng nhập vào tham số thứ ba : ').strip()

    if floatRegex(a) and floatRegex(b) and floatRegex(c) :
        def resolve(a, b, c):
            delta = math.pow(float(b), 2) - 4*float(a)*float(c)
            global result 
            if (delta < 0):
                result = 'vô nghiệm'
            elif (delta == 0):
                x = -float(b)/ (2 * float(a))
                result = f'có nghiệm kép {int(x)}'
            else :
                x1 = (-float(b) + math.sqrt(delta)) / 2* float(a)
                x2 = (-float(b) - math.sqrt(delta)) / 2* float(a)
                result = (f'có 2 nghiệm là:  \n x1={int(x1)} \n x2={int(x2)}')
            return result
        print(f'Phương trình {a}x2 + {b}x + {c} : {resolve(a, b, c)}')
        break
    else :
        print('Vui lòng nhập tham số là các giá trị số thực!')
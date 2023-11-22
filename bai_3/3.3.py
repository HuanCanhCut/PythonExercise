import math
import re 

# Biểu thức chính quy kiểm tra giá trị có phải là một số thực hay không
regex = r'^-?\d+(\.\d+)?$'

while(True):
    a = input('Vui lòng nhập vào tham số thứ nhất : ').strip()
    b = input('Vui lòng nhập vào tham số thứ hai : ').strip()
    c = input('Vui lòng nhập vào tham số thứ ba : ').strip()

    if re.fullmatch(regex, a) and  re.fullmatch(regex, b) and  re.fullmatch(regex, c) :
        delta = math.pow(float(b), 2) - 4*float(a)*float(c)
        if (delta < 0):
            result = 'vô nghiệm'
        elif (delta == 0):
            x = -float(b)/ (2 * float(a))
            result = f'có nghiệm kép {int(x)}'
        else :
            x1 = (-float(b) + math.sqrt(delta)) / 2* float(a)
            x2 = (-float(b) - math.sqrt(delta)) / 2* float(a)
            result = (f'có 2 nghiệm là:  \n x1={int(x1)} \n x2={int(x2)}')
        print(f'Phương trình {a}x2 + {b}x + {c} : {result}')
        break
    else :
        print('Vui lòng nhập tham số là các giá trị số thực! \n')
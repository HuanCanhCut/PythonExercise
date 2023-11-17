from regex import floatRegex

while(True):
    a = input('Nhập vào tham số thứ nhất: ').strip()
    b = input('Nhập vào tham số thứ hai : ').strip()
    if (floatRegex(a)) and (floatRegex(b)) :
        
        # hàm tính toán
        def resolve (a, b):
            result = -float(b) / float(a)
            return result
        
        print(f'Nghiệm của phương trình {a}x + {b} là : {resolve(a, b)}')
        break
    else : 
        print('Vui lòng nhập các tham số là một số nguyên')     
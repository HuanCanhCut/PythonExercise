while(True):
    firstParam = input('Nhập vào tham số thứ nhất: ').strip()
    lastParam = input('Nhập vào tham số thứ hai : ').strip()
    if (firstParam.isdigit()) and (lastParam.isdigit()) :
        
        # hàm tính toán
        def resolve (first, last):
            result = -float(last) / float(first)
            return result
        
        print(f'Nghiệm của phương trình {firstParam}x + {lastParam} là : {resolve(firstParam, lastParam)}')
        break
    else : 
        print('Vui lòng nhập các tham số là một số nguyên')     
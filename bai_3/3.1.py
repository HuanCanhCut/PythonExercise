while(True):
    num = input(__prompt='Nhập vào 3 số bất kì: ').strip()
    numArr = num.split(' ')
    if len(numArr) == 3 :
        for i in numArr :
            print(f'Giá trị nhỏ nhất trong {numArr} là {min(i)}')
            break
        break;
    else : 
        print('Vui lòng nhập vào 3 số')
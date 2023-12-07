sum = 0

while True: 
    n = float(input('Nhập 1 số n bất kì: '))

    #  Nếu n âm thì hiển thị ra thì bắt ngƣời dùng nhập lại
    if n > 0:
        #  Nếu n nguyên dƣơng và là số chẵn thì tính và hiển thị ra tổng các số lẻ từ 1  n
        if (n % 2 == 0):
            for i in range(0, int(n) + 1):
                if i % 2 != 0:
                    sum += i
            print('Tổng các số lẻ từ 1 -> n là : ', sum)

        # Nếu n nguyên dƣơng và là số lẻ thì tính và hiển thị ra tổng các số chẵn từ 1  n
        if (n % 2 != 0): 
            for i in range(0, int(n) + 1):
                if i % 2 == 0:
                    sum += i
            print('Tổng các số lẻ từ 1 -> n là : ', sum)
    
        #  Nếu n nguyên thì hiển thị ra các số không chia hết cho 3 nằm trong đoạn [1-N].
        if n.is_integer():
            # danh sách các số không chia hết cho 3
            notDivisible = []
            for i in range(1, int(n) + 1):
                if i % 3 != 0:
                    notDivisible.append(i)
            print('Các số không chia hết cho 3 là : \n', notDivisible)    

        #  Nếu n nguyên thì hiển thị ra màn hình giá trị các biểu thức sau:
        if n.is_integer():
                s3 = 1
                for i in range(1, int(n) + 1):
                    s3 *= (2*i - 1) / (2 * i)
                print(f'S3: {s3}')
                    
        break
    else: 
        print('Vui lòng nhập số n lớn hơn 0. \n')

print('\n')
# Xây dựng chƣơng trình nhập vào từ bàn phím hai số nguyên dƣơng x, n (10<x,
# n<20). Tính và hiển thị ra màn hình tổng: S2 = x+x/2+x/3+...+x/n.
while True:
    n = int(input('Nhập vào số nguyên dương n (n < 20): '))
    x = int(input('Nhập vào số nguyên dương x (x > 10):'))
    
    if (n, x > 0 and n < 20 and x > 10) :
        s2 = 0
        for i in range (1, n + 1):
            s2 +=  x / i
        print('s2:', s2)
        break
    else :
        print('Vui lòng nhập lại!')

print('\n')

#  Nhập một số n nguyên dƣơng từ bàn phím.

while True:
    n = input('Nhập vào số nguyên dương n: ')
    if (int(n) > 0):
        print(f'{n} có {len(str(n))} ký tự')
        total = 0
        for i in n:
            total += int(i)
        print(f'Tổng các ký tự là : {total}')
        break
    else :
        print('Vui lòng nhập n > 0')  
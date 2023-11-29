while (True):
    n = input('Nhập vào số tự nhiên: ')
    if (n.isdigit()):
        n = int(n)
        for i in range(1, n+1):
            isPrime = True
            for j in range (2, i):
                if (i % j == 0):
                    isPrime = False
                    break
            if (isPrime == True):
                print(f'{i} là số nguyên tố')
        break
    else:
        print(f'{n} không phải là một số tự nhiên, Vui lòng nhập lại!')

while (True):
    n = input('Nhập vào số tự nhiên: ')
    if (n.isdigit()):
        n = int(n)
        for i in range(1, n+1):
            break
    else:
        print(f'{n} không phải là một số tự nhiên, Vui lòng nhập lại!')

x = int(input('Nhập vào x : '))

def checkPrime (x):
    for i in range(2, x):
        if x % i == 0:
            print(f'{x} không phải là số nguyên tố!')
            return
    print(f'{x} là số nguyên tố!')

checkPrime(x)


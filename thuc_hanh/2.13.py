
n = int(input('Nhập vào số tự nhiên: '))
    
primeArr = []

for i in range(1, n+1):
    isPrime = True
    for j in range (2, i):
        if (i % j == 0):
            isPrime = False
            break
    if (isPrime == True):
        primeArr.append(i)
        
print(f'Danh sách các số nguyên tố từ 1 đến {n} là: \n {primeArr}')
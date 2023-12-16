def primeLogger (n):
    primeArr = []

    for i in range(1, n+1):
        isPrime = True
        for j in range (2, i):
            if (i % j == 0):
                isPrime = False
                break

        if (isPrime == True):
            primeArr.append(i)

    return primeArr
            
print(f'Danh sách các số nguyên tố từ 1 đến {100} là: \n {primeLogger(100)}')
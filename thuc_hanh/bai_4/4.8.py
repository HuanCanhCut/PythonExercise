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
    
with open('./SoNguyenTo.txt', 'w') as file:
    for i in primeLogger(1000):
        file.write(f'{str(i)} \n')
        

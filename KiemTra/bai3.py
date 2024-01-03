L = []

while (True):
    n = input('Nhập vào số n: ')
    if not n :
        break

    L.append(int(n))

result = 0

for i in range(1, len(L) + 1):
    if (i % 2) == 0:
        result += i
    
print(result)

def total (n):
    result = 0
    for i in range(0, (n) + 1):
        result += 1 / (2 * i + 1)
    return result
n = int(input('Nhập vào tham số n: '))

print(f'Tổng của biểu thức trên là : {total(n)}')
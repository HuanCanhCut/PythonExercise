def sum (n):
    s3 = 0
    for i in range(0, n):
        s3 += (1 / (2 * i + 1))
    return s3

n = int(input('Nhập n : '))

print(f'Kết quả là : {sum(n)}')
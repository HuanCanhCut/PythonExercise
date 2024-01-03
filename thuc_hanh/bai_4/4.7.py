l = []

while (True):
    intNumber = input('Nhập vao số nguyên dương: ').strip()

    if (not intNumber.isdigit()):
        break

    l.append(int(intNumber))

print(l)
print(f'Số lớn nhất trong dãy trên là {max(l)}')
    
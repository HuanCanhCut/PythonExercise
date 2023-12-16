def formatString (str):
    rawArr = str.split(' ')
    newArr = []
    for i in rawArr:
        if (i.strip() != ''):
            newArr.append(i)
    return ' '.join(newArr)

initString = input('Nhập vào một chuỗi: ')

print(f'Chuỗi sau khi được định dạng: {formatString(initString).title()}')



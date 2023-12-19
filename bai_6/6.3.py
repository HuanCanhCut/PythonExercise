def formatString (str):
    # Mảng dữ liệu thô
    rawArr = str.split(' ')
    # Mảng dữ liệu mới khi đã được xử lí
    newArr = []
    for i in rawArr:
        if (i.strip() != ''):
            newArr.append(i)
    # Chuyển đổi mảng đã được xử lí thành chuỗi
    print(newArr)
    return ' '.join(newArr)

initString = input('Nhập vào một chuỗi: ')

print(f'Chuỗi sau khi được định dạng: {formatString(initString).title()}')

from regex import floatRegex
data = [
    {
        'value': 'Xuất sắc',
        'min': 90,
        'max': 100,
    },
    {
        'value': 'Giỏi',
        'min': 80,
        'max': 90,
    },
    {
        'value': 'Khá',
        'min': 65,
        'max': 80,
    },
    {
        'value': 'Trung bình',
        'min': 50,
        'max': 65,
    },
    {
        'value': 'Yếu',
        'min': 0,
        'max': 50,
    },
]

studentCode = input('Nhập vào mã sinh viên: ')
fullName = input('Nhập vào tên đầy đủ: ')

while(True):
    training = input('Nhập vào điểm rèn luyện: ')

    if floatRegex(training):
        # convert training to float
        training = float(training)
        
        if (training <= 100) and (training >= 0):
            for i in data:
                if (training >= i['min'] ) and (training < i['max']):
                    value = i['value']
                    print(f'{fullName} - Mã sinh viên: {studentCode} ====> có hạnh kiểm : {value}')
                    break
            break
        else:
            print('Giá trị nhập vào của điểm đào tạo phải trên <= 100 hoặc >= 0, Vui lòng nhập lại!')
    else : 
        print('Giá trị nhập vào phải là một số thực. Vui lòng nhập lại !')
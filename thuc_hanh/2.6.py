import re

hoTen = input('Nhập tên của chủ hộ')

# biểu thức chính quy kiểm tra xem giá trị nhập vào có phải là số thực lớn hơn 0 hay không
regex = r'^(?:0|[1-9]\d*)(?:\.\d+)?$'


while (True):
    chiso1 = input('Nhập vào số điện tháng trước: ').strip()
    chiso2 = input('Nhập vào số điện tháng này: ').strip()

    if (re.match(regex, chiso1)) and (re.match(regex, chiso2)):
        chiso1 = float(chiso1)
        chiso2 = float(chiso2)
        break
    else :
        print('Số điện nhập vào phải là một số thực lớn hơn 0 \n')

soKW = chiso2 - chiso1

if (soKW <= 60) :
    soTien = soKW * 5
elif (soKW >= 61 and soKW <= 160):
    soKWvuot = soKW - 60
    soTien = 60 * 5 + soKWvuot * 8
else :
    soKWvuot = soKW - 160
    soTien = 60 * 5 + 100 * 8 + soKWvuot * 10
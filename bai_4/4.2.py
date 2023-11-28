from datetime import  datetime

date = datetime.now()

isLoop = True

while(isLoop):
    birth = input('Nhập vào năm sinh của bạn : ')
    currentYear = date.year
    for i in birth :
        if (i.isdigit()):
            birth = int(birth)
            if (birth > 1900) and (birth <= currentYear):
                print(f'Năm sinh của bạn là: {birth}')
                isLoop = False
                break
            else :
                print(f'Năm sinh phải lớn hơn 1900 và nhỏ hơn {currentYear} \n')
                break
        else :
            print('Năm sinh nhập vào chứa chuỗi kí tự, vui lòng nhập lại! \n')
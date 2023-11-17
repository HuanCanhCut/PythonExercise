import re

# biểu thức chính quy
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


while(True):
    emailValue = input('Nhap email cua ban : ')

    if (re.fullmatch(regex, emailValue)):
        print('Valid email')
        break
    else :
        print('invalid email, please try again')
        # break

        
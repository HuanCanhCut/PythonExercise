from regex import isInteger
from regex import isEmail

scmt = input('Nhập số chứng minh: ')

if (isInteger(scmt)):
    if (len(scmt) >= 9 and len(scmt) <= 11):
        print('Số chứng minh hợp lệ! ')
    else :
        print('Số chứng minh phải dài từ 9 đến 11 ký tự!')
else :
    print('Số chứng minh thư không hợp lệ!')    


se = input('Nhập địa chỉ email: ')

if(isEmail(se)):
    print('Email hợp lệ!')
else : 
    print('Email không hợp lệ!')

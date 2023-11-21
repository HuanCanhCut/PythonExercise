# 2.9 trang 72

cccdID = input('nhap so can cuoc cong dan : ')
while(True):
        
    for char in cccdID:
        if (char.isdigit()):
            if(len(cccdID) >= 9) and len(cccdID) <= 11:
                print(f'so chung minh cua ban la {cccdID}')
                break
            else:
                print('so chung minh phai co do dai tu 9 den 11 ky tu')
        else :
            print('Gia tri nhap vao chua chuoi ki tu!, vui long nhap lai')
    break        
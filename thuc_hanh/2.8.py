import re 

# biểu thức chính quy kiểm tra xem giá trị nhập vào có phải là số thực lớn và lớn hơn 0 hay không
regex = r'^(?:0|[1-9]\d*)(?:\.\d+)?$'

while (True):
    chieuDai : input('Nhập vào chiều dài của hình chữ nhật: ').strip()
    chieuRong : input('Nhập vào chiều rộng của hình chữ nhật: ').strip()
    
    # kiểm tra xem giá trị nhập vào có chứa toàn số thực lớn hơn 0 hay không
    if (re.fullmatch(regex, chieuDai)) and (re.fullmatch(regex, chieuRong)):
        chuVi = (chieuDai + chieuRong) * 2
        dienTich = chieuDai * chieuRong
        
        print(f'Chu vi của hình chữ nhật là: {chuVi}')
        print(f'Diện tích của hình chữ nhật là: {dienTich}')
        break
    else :
        print('Giá trị nhập vào chứa kí tự khác ngoài số thực, vui lòng nhập lại \n')
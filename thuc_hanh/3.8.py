danhSachLop = []

while True:
    account = input('Nhập vào tên tài khoản: ')
    if (not account):
        break
    
    danhSachLop.append(account)
        
for i in range (0, len(danhSachLop)):
    print(f'{i + 1}. {danhSachLop[i]}')

TK = 'TK131'

if (TK in danhSachLop):
    print(f'Trong danh sách có tài khoản {TK}')
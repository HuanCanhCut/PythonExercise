L = []

while True:
    maSv = (input('\nNhập mã sinh viên: '))
    
    if not maSv:
        break


    tenSv = input('Nhập tên sinh: viên: ')
    namSinh = (input('Nhập năm sinh: '))
    queQuan = input('Nhập quê quán: ')


    
    L.append(int(maSv))
    L.append(tenSv)
    L.append(int(namSinh))
    L.append(queQuan)

filePath = 'data.txt'

print(L)

for i in L:
    with open(filePath, mode='a', encoding='utf-8') as file:
        file.write(f'{str(i)} \n' )
L = []

while True:
    maSv = (input('\nNhập mã sinh viên: '))
    
    if not maSv:
        break


    tenSv = input('Nhập tên sinh: viên: ')
    namSinh = (input('Nhập năm sinh: '))
    queQuan = input('Nhập quê quán \n')


    duLieu = {
        'Mã sinh viên': int(maSv),
        'Tên sinh viên': tenSv,
        'Năm sinh': int(namSinh),
        'Quê quán': queQuan,
    }
    
    L.append(duLieu)

print(L)
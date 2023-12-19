danhSachHangHoa = []

while True:
    # Thêm danh sách hàng hóa có sẵn
    hangCoSan = input('Nhập vào mặt hàng trong kho: ')
    if (not hangCoSan):
        break

    danhSachHangHoa.append(hangCoSan)

hangX = input('Nhập vào mặt hàng cần tìm: ')


if (hangX in danhSachHangHoa) :
    hangB = input(f'Nhập tên cần sửa cho mặt hàng {hangX}: ')
    # Tìm vị trí của hàng X và gán nó lại thành hàng B
    indexHangX = danhSachHangHoa.index(hangX)
    danhSachHangHoa[indexHangX] = hangB
    
else :
    danhSachHangHoa.append(hangX)

print(danhSachHangHoa)

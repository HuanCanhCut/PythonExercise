hoTen = input('Chủ hộ: ')
chiSo1 = float(input('chỉ số điện kế tháng trước: '))
chiSo2 = float(input('chỉ số điện kế tháng này: '))
soKW = chiSo2 - chiSo1
if soKW<=60:
    soTien = soKW*5
elif 61<=soKW<=160:
    soTien = 60*5+(soKW-60)*8
else:
    SoTien = 60*5+100*8+(soKW-60)*10 
print(f"họ và tên chủ hộ là: {hoTen}")
print(f"chỉ số điện kế tháng trước là: {chiSo1}")
print(f"chỉ số điện kế tháng này là: {chiSo2}")
print(f"số KW điện đã dùng trong tháng là: {soKW}")
print(f"tiền điện tháng này của hộ là: {soTien} đồng")
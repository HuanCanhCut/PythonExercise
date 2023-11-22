hoTenSV = input('Nhập tên của sinh viên: ')
maSV = input('Nhập vào mã sinh viên: ')
diemRenLuyen = float(input('Nhập điểm rèn luyện của sinh viên: '))

if (diemRenLuyen >= 90):
    hanhKiem = 'Xuất sắc'

elif (diemRenLuyen < 90 and diemRenLuyen >= 80):
    hanhKiem = 'Giỏi'

elif (diemRenLuyen < 80 and diemRenLuyen >= 65):
    hanhKiem = 'Khá'

elif (diemRenLuyen < 65 and diemRenLuyen >= 50):
    hanhKiem = 'Trung bình'

else:
    hanhKiem = 'Yếu'

print(f'Sinh viên {hoTenSV} với mã sv : {maSV} có số điểm rèn luyện : {diemRenLuyen} đạt hạnh kiểm: {hanhKiem.upper()}')



thoiGianHienTai = input('Nhập vào thời gian dạng hh:mm:ss: ')
k = float(input('Nhập số giây cộng thêm: '))

mangThoiGian = thoiGianHienTai.split(':')

tongSoGiay = int(mangThoiGian[0]) * 3600 int(mangThoiGian[1]) * 60 + int(mangThoiGian[2]) + k

gioMoi = tongSoGiay // 3600
phutMoi = (tongSoGiay - (gioMoi * 3600)) // 60
giayMoi = (tongSoGiay - (gioMoi * 3600) - (phutMoi * 60))

print(f'Thời gian mới là : {gioMoi}:{phutMoi}:{giayMoi}')

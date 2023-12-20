import pandas as pd

# Hàm tính tiền điện
def handleElectricityBills(kiloWatage):
    VAT = 10 / 100

    # Cấu trúc dữ liệu để lưu trữ giá và ngưỡng lớn nhất của từng bậc
    price = [
        {"max": 100, "price": 1450},
        {"max": 150, "price": 1750},
        {"max": 250, "price": 2000},
        {"max": float('inf'), "price": 2500},
    ]

    # Tính toán tiền điện
    billBeforeVAT = 0

    for bac in price:
        # số điện bậc hiện tại
        currentLevel = min(kiloWatage, bac["max"])
        billBeforeVAT += currentLevel * bac["price"]
        kiloWatage -= currentLevel

        if kiloWatage <= 0:
            break

    # Tổng tiền điện sau VAT
    billAfterVAT = billBeforeVAT + billBeforeVAT * VAT

    return f'{int(billAfterVAT)} VND'

# Danh sách các hộ gia đình
hoursHolds = []
buildingNumbers = []

# Nhập dữ liệu từ các hộ gia đình
while True:
    roomNumber = input('Nhập số phòng: ')

    if not roomNumber:
        break
    
    while True:
        buildingNumber = input('Nhập số hiệu tòa nhà: ')
        if len(buildingNumber) > 0:
            break

    while True:
        headerHouseHold = input('Nhập tên chủ hộ: ')
        if len(headerHouseHold) > 0:
            break
        
    while True:
        try:
            kiloWatage = float(input('Nhập số kW điện trong một tháng: '))
            print('')
            if kiloWatage >= 0:
                break
        except Exception as e:
            print(e)

    hoursHolds.append({
        'buildingNumber': buildingNumber,
        'roomNumber': roomNumber,
        'headerHouseHold': headerHouseHold,
        'kiloWatage': kiloWatage,
    })

    buildingNumbers.append((buildingNumber))

# Mở file và viết dữ liệu
for buildingNumber in buildingNumbers:
    file_path = f'{buildingNumber}.txt'
    with open(file_path, 'a', encoding='utf-8') as file:
        # Viết dòng tiêu đề nếu file rỗng
        if file.tell() == 0:
            file.write("Tòa nhà\t\tPhòng\t\tTên chủ hộ\tSDTT\t\t\tTiền điện phải trả\n")

        # Viết dữ liệu
        for hoursHold in hoursHolds:
            if buildingNumber == hoursHold['buildingNumber']:
                value = '\t\t\t'.join([
                    hoursHold['buildingNumber'],
                    hoursHold['roomNumber'],
                    hoursHold['headerHouseHold'],
                    str(hoursHold['kiloWatage']),
                    str(handleElectricityBills(hoursHold['kiloWatage']))
                ])

                file.write(value + '\n')

print('Dữ liệu đã được ghi vào file.')

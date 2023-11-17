allowances = [
    {
        'position': 'Giám đốc',
        'price': 5000000
    },
    {
        'position': 'Phó giám đốc',
        'price': 5000000
    },
    {
        'position': 'Trưởng phòng',
        'price': 5000000
    },
]

fullName = input('Nhập họ và tên: ').strip()
position = input('Nhập chức vụ: ').strip()

for allowance in allowances:
    if (position.lower() == allowance['position'].lower()):
        price = allowance['price']
        print(f'{fullName} được phụ cấp: {price}')
    else :
        print(f'{fullName} không được phụ cấp')
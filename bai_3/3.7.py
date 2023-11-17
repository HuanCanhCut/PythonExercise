from regex import floatRegex

data = [
    {
        'min': 0,
        'max': 50,
        'price': 2000
    },
    {
        'min': 50,
        'max': 150,
        'price': 2500
    },
    {
        'min': 150,
        'max': 250,
        'price': 3000
    },
    {
        'min': 250,
        'max': 400,
        'price': 3500
    },
    {
        'min': 400,
        'price': 4000
    },
]

while (True):
    kWh = input('Nhập vào số điện tiêu thụ (kW/h) : ')

    if (floatRegex(kWh)) :
        kWh = float(kWh)
        for i in data: 
            def resolve (i, kWh):
                result = kWh * i['price']
                print(f'Số tiền mà bạn tiêu thụ trong tháng này là : {result}')

            if 'max' in i:
                if (kWh > i['min']) and (kWh <= i['max']) :
                    resolve(i, kWh)
                    break
            else :
                if (kWh > i['min']):
                    resolve(i, kWh)
                    break

        break
    else :
        print('Vui lòng nhập vào giá trị là một số thực')

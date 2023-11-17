currentCoins = 5000000
currentInterest =  0.8 
name = 'An'

month = int(input('nhap so thang gui lai: '))

print(f'ten nguoi gui {name}')
print(f'so tien gui {currentCoins} vnd')
print(f'lai suat / thang : {currentInterest} %')
print(f'so tien lai {currentCoins * (currentInterest / 100) * month}')